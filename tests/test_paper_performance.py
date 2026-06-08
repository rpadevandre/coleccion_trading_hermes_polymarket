from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.models import Market, ScoreBreakdown
from polymarket_research.paper import (
    PaperTradingConfig,
    close_paper_position,
    maybe_open_paper_position,
    performance_summary,
)


def _market(market_id: str = "m-close-1", price: float = 0.25) -> Market:
    return Market(
        market_id=market_id,
        question="Will this paper market resolve yes?",
        condition_id="0xclose",
        slug="paper-close-test",
        outcomes=["Yes", "No"],
        outcome_prices=[price, 1 - price],
        clob_token_ids=["yes-token", "no-token"],
        volume=50_000,
        liquidity=10_000,
        active=False,
        closed=True,
    )


def _score(total: int = 90) -> ScoreBreakdown:
    return ScoreBreakdown(
        total_score=total,
        recommendation="RESEARCH_CANDIDATE",
        dimensions={"test": 1},
        reasoning=["test signal"],
    )


def test_close_paper_position_win_calculates_profit(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    market = _market(price=0.25)
    maybe_open_paper_position(conn, market, _score(), config=PaperTradingConfig(bankroll=1_000))

    closed = close_paper_position(conn, market.market_id, winning_side="YES")

    assert closed is not None
    assert closed["status"] == "CLOSED"
    assert closed["exit_price"] == 1.0
    assert closed["pnl"] == 60.0  # $20 at 0.25 => 80 shares, payout $80, profit $60

    row = conn.execute("SELECT status, exit_price, pnl FROM paper_positions WHERE market_id = ?", (market.market_id,)).fetchone()
    assert row == ("CLOSED", 1.0, 60.0)


def test_close_paper_position_loss_calculates_loss(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    market = _market(price=0.25)
    maybe_open_paper_position(conn, market, _score(), config=PaperTradingConfig(bankroll=1_000))

    closed = close_paper_position(conn, market.market_id, winning_side="NO")

    assert closed is not None
    assert closed["exit_price"] == 0.0
    assert closed["pnl"] == -20.0


def test_performance_summary_reports_closed_roi_and_win_rate(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)

    winner = _market(market_id="winner", price=0.25)
    loser = _market(market_id="loser", price=0.5)
    maybe_open_paper_position(conn, winner, _score(), config=PaperTradingConfig(bankroll=1_000))
    maybe_open_paper_position(conn, loser, _score(), config=PaperTradingConfig(bankroll=1_000))
    close_paper_position(conn, "winner", winning_side="YES")
    close_paper_position(conn, "loser", winning_side="NO")

    summary = performance_summary(conn, bankroll=1_000)

    assert summary["closed_positions"] == 2
    assert summary["wins"] == 1
    assert summary["losses"] == 1
    assert summary["realized_pnl"] == 40.0
    assert summary["roi_pct"] == 100.0  # $40 P&L on $40 closed stake
    assert summary["win_rate_pct"] == 50.0
