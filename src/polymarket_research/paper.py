"""Paper-trading simulation for Polymarket research signals.

This module uses fictional bankroll only. It never connects to wallets and never
places orders. Its purpose is to test whether scanner signals would have become
interesting enough to justify later manual review.
"""

from __future__ import annotations

from dataclasses import dataclass
import sqlite3

from .models import Market, ScoreBreakdown


@dataclass(frozen=True)
class PaperTradingConfig:
    bankroll: float = 1_000.0
    min_score: int = 80
    max_risk_per_trade_pct: float = 0.02
    max_total_exposure_pct: float = 0.20
    min_entry_price: float = 0.02
    max_entry_price: float = 0.98


@dataclass(frozen=True)
class PaperPosition:
    market_id: str
    side: str
    entry_price: float
    stake: float
    shares: float
    score: int
    status: str = "OPEN"


def _open_exposure(conn: sqlite3.Connection) -> float:
    row = conn.execute("SELECT COALESCE(SUM(stake), 0) FROM paper_positions WHERE status = 'OPEN'").fetchone()
    return float(row[0] or 0.0)


def _has_open_position(conn: sqlite3.Connection, market_id: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM paper_positions WHERE market_id = ? AND status = 'OPEN' LIMIT 1",
        (market_id,),
    ).fetchone()
    return row is not None


def _ensure_market_row(conn: sqlite3.Connection, market: Market) -> None:
    conn.execute(
        """
        INSERT OR IGNORE INTO markets (
            market_id, question, condition_id, slug, outcomes_json,
            outcome_prices_json, clob_token_ids_json, volume, liquidity,
            active, closed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        market.to_db_tuple(),
    )


def _select_side_and_price(market: Market) -> tuple[str, float] | None:
    if len(market.outcome_prices) < 2:
        return None
    yes_price = float(market.outcome_prices[0])
    return "YES", yes_price


def maybe_open_paper_position(
    conn: sqlite3.Connection,
    market: Market,
    score: ScoreBreakdown,
    *,
    config: PaperTradingConfig | None = None,
) -> PaperPosition | None:
    """Open one fictional position when a signal passes risk gates.

    The sizing is intentionally conservative: per-trade stake is capped and total
    open exposure cannot exceed the configured bankroll percentage.
    """

    config = config or PaperTradingConfig()
    if score.total_score < config.min_score:
        return None
    if score.recommendation != "RESEARCH_CANDIDATE":
        return None
    if _has_open_position(conn, market.market_id):
        return None

    _ensure_market_row(conn, market)

    side_price = _select_side_and_price(market)
    if side_price is None:
        return None
    side, entry_price = side_price
    if not (config.min_entry_price <= entry_price <= config.max_entry_price):
        return None

    max_total_exposure = round(config.bankroll * config.max_total_exposure_pct, 2)
    current_exposure = _open_exposure(conn)
    remaining_exposure = round(max_total_exposure - current_exposure, 2)
    if remaining_exposure <= 0:
        return None

    per_trade_cap = round(config.bankroll * config.max_risk_per_trade_pct, 2)
    stake = min(per_trade_cap, remaining_exposure)
    if stake <= 0:
        return None

    shares = stake / entry_price
    position = PaperPosition(
        market_id=market.market_id,
        side=side,
        entry_price=round(entry_price, 4),
        stake=round(stake, 2),
        shares=shares,
        score=score.total_score,
    )
    conn.execute(
        """
        INSERT INTO paper_positions (market_id, side, entry_price, stake, shares, score, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            position.market_id,
            position.side,
            position.entry_price,
            position.stake,
            position.shares,
            position.score,
            position.status,
        ),
    )
    return position


def portfolio_summary(conn: sqlite3.Connection, *, bankroll: float = 1_000.0) -> dict[str, float | int]:
    open_positions = conn.execute("SELECT COUNT(*) FROM paper_positions WHERE status = 'OPEN'").fetchone()[0]
    exposure = _open_exposure(conn)
    return {
        "bankroll": round(bankroll, 2),
        "open_positions": int(open_positions),
        "open_exposure": round(exposure, 2),
        "available_cash": round(bankroll - exposure, 2),
    }
