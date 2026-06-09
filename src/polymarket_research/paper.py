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


def _realized_pnl(conn: sqlite3.Connection) -> float:
    row = conn.execute("SELECT COALESCE(SUM(pnl), 0) FROM paper_positions WHERE status = 'CLOSED'").fetchone()
    return float(row[0] or 0.0)


def _ensure_account(conn: sqlite3.Connection, bankroll: float) -> tuple[float, float]:
    """Return `(initial_bankroll, cash_balance)`, creating a persistent account if needed.

    Existing databases are migrated conservatively: cash starts as initial bankroll
    minus open stake plus already-realized P&L, so old open positions do not get a
    fresh infinite bankroll after migration.
    """

    row = conn.execute("SELECT initial_bankroll, cash_balance FROM paper_account WHERE id = 1").fetchone()
    if row is not None:
        initial = float(row[0])
        _backfill_legacy_ledger_if_empty(conn, initial)
        return initial, float(row[1])

    initial = round(float(bankroll), 2)
    cash = round(initial - _open_exposure(conn) + _realized_pnl(conn), 2)
    conn.execute(
        "INSERT INTO paper_account (id, initial_bankroll, cash_balance) VALUES (1, ?, ?)",
        (initial, cash),
    )
    _backfill_legacy_ledger_if_empty(conn, initial)
    return initial, cash


def _set_cash_balance(conn: sqlite3.Connection, cash_balance: float) -> None:
    conn.execute(
        "UPDATE paper_account SET cash_balance = ?, updated_at = CURRENT_TIMESTAMP WHERE id = 1",
        (round(cash_balance, 2),),
    )


def _record_ledger(
    conn: sqlite3.Connection,
    *,
    event_type: str,
    market_id: str,
    position_id: int,
    amount: float,
    cash_balance_after: float,
    note: str | None = None,
) -> None:
    conn.execute(
        """
        INSERT INTO paper_ledger (event_type, market_id, position_id, amount, cash_balance_after, note)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (event_type, market_id, position_id, round(amount, 2), round(cash_balance_after, 2), note),
    )


def _backfill_legacy_ledger_if_empty(conn: sqlite3.Connection, initial_bankroll: float) -> None:
    ledger_count = conn.execute("SELECT COUNT(*) FROM paper_ledger").fetchone()[0]
    if int(ledger_count or 0) > 0:
        return

    rows = conn.execute(
        """
        SELECT id, market_id, stake, status, payout, pnl, opened_at, closed_at
        FROM paper_positions
        ORDER BY opened_at ASC, id ASC
        """
    ).fetchall()
    if not rows:
        return

    cash = round(float(initial_bankroll), 2)
    for row in rows:
        position_id, market_id, stake, status, payout, pnl, opened_at, closed_at = row
        cash = round(cash - float(stake), 2)
        _record_ledger(
            conn,
            event_type="LEGACY_OPEN",
            market_id=str(market_id),
            position_id=int(position_id),
            amount=-float(stake),
            cash_balance_after=cash,
            note=f"Backfilled from pre-ledger paper position opened_at={opened_at}",
        )
        if str(status).upper() == "CLOSED":
            credit = float(payout) if payout is not None else float(stake) + float(pnl or 0.0)
            cash = round(cash + credit, 2)
            _record_ledger(
                conn,
                event_type="LEGACY_CLOSE",
                market_id=str(market_id),
                position_id=int(position_id),
                amount=credit,
                cash_balance_after=cash,
                note=f"Backfilled from pre-ledger paper position closed_at={closed_at}",
            )


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
            active, closed, end_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

    _, cash_balance = _ensure_account(conn, config.bankroll)
    if cash_balance <= 0:
        return None

    per_trade_cap = round(config.bankroll * config.max_risk_per_trade_pct, 2)
    stake = min(per_trade_cap, remaining_exposure, cash_balance)
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
    cursor = conn.execute(
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
    position_id = cursor.lastrowid
    if position_id is None:
        raise RuntimeError("SQLite did not return paper position id")
    cash_after_open = round(cash_balance - position.stake, 2)
    _set_cash_balance(conn, cash_after_open)
    _record_ledger(
        conn,
        event_type="OPEN",
        market_id=position.market_id,
        position_id=position_id,
        amount=-position.stake,
        cash_balance_after=cash_after_open,
        note=f"Opened {position.side} at {position.entry_price}",
    )
    return position


def portfolio_summary(conn: sqlite3.Connection, *, bankroll: float = 1_000.0) -> dict[str, float | int]:
    open_positions = conn.execute("SELECT COUNT(*) FROM paper_positions WHERE status = 'OPEN'").fetchone()[0]
    exposure = _open_exposure(conn)
    initial_bankroll, cash_balance = _ensure_account(conn, bankroll)
    realized_pnl = round(_realized_pnl(conn), 2)
    return {
        "bankroll": round(initial_bankroll, 2),
        "open_positions": int(open_positions),
        "open_exposure": round(exposure, 2),
        "available_cash": round(cash_balance, 2),
        "realized_pnl": realized_pnl,
        "equity_before_mark_to_market": round(cash_balance + exposure, 2),
    }


def close_paper_position(conn: sqlite3.Connection, market_id: str, *, winning_side: str) -> dict[str, float | str] | None:
    """Close an open fictional position against a resolved winning side.

    `winning_side` is expected to be `YES` or `NO`. This is paper-only: payout
    is simulated as binary 1.0/0.0 against the side we opened.
    """

    winning_side = winning_side.upper()
    if winning_side not in {"YES", "NO"}:
        raise ValueError("winning_side must be YES or NO")

    row = conn.execute(
        """
        SELECT id, side, stake, shares
        FROM paper_positions
        WHERE market_id = ? AND status = 'OPEN'
        ORDER BY opened_at ASC
        LIMIT 1
        """,
        (market_id,),
    ).fetchone()
    if row is None:
        return None

    position_id, side, stake, shares = row
    exit_price = 1.0 if str(side).upper() == winning_side else 0.0
    payout = round(float(shares) * exit_price, 2)
    pnl = round(payout - float(stake), 2)
    outcome = "WIN" if pnl > 0 else "LOSS" if pnl < 0 else "PUSH"
    event_type = f"CLOSE_{outcome}"
    _, cash_balance = _ensure_account(conn, 1_000.0)
    cash_after_close = round(cash_balance + payout, 2)

    conn.execute(
        """
        UPDATE paper_positions
        SET status = 'CLOSED', closed_at = CURRENT_TIMESTAMP, exit_price = ?, payout = ?, pnl = ?,
            winning_side = ?, outcome = ?
        WHERE id = ?
        """,
        (exit_price, payout, pnl, winning_side, outcome, position_id),
    )
    _set_cash_balance(conn, cash_after_close)
    _record_ledger(
        conn,
        event_type=event_type,
        market_id=market_id,
        position_id=int(position_id),
        amount=payout,
        cash_balance_after=cash_after_close,
        note=f"Resolved winner {winning_side}; position side {side}; outcome {outcome}",
    )
    return {
        "market_id": market_id,
        "status": "CLOSED",
        "winning_side": winning_side,
        "outcome": outcome,
        "exit_price": exit_price,
        "payout": payout,
        "pnl": pnl,
    }


def performance_summary(conn: sqlite3.Connection, *, bankroll: float = 1_000.0) -> dict[str, float | int]:
    closed_positions, wins, losses, realized_pnl, closed_stake = conn.execute(
        """
        SELECT
            COUNT(*),
            SUM(CASE WHEN pnl > 0 THEN 1 ELSE 0 END),
            SUM(CASE WHEN pnl < 0 THEN 1 ELSE 0 END),
            COALESCE(SUM(pnl), 0),
            COALESCE(SUM(stake), 0)
        FROM paper_positions
        WHERE status = 'CLOSED'
        """
    ).fetchone()
    closed_positions = int(closed_positions or 0)
    wins = int(wins or 0)
    losses = int(losses or 0)
    realized_pnl = round(float(realized_pnl or 0.0), 2)
    closed_stake = float(closed_stake or 0.0)
    roi_pct = round((realized_pnl / closed_stake) * 100, 2) if closed_stake else 0.0
    win_rate_pct = round((wins / closed_positions) * 100, 2) if closed_positions else 0.0
    open_summary = portfolio_summary(conn, bankroll=bankroll)
    return {
        **open_summary,
        "closed_positions": closed_positions,
        "wins": wins,
        "losses": losses,
        "realized_pnl": realized_pnl,
        "closed_stake": round(closed_stake, 2),
        "roi_pct": roi_pct,
        "win_rate_pct": win_rate_pct,
    }
