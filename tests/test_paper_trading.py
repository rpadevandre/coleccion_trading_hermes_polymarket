from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.models import Market, ScoreBreakdown
from polymarket_research.paper import PaperTradingConfig, close_paper_position, maybe_open_paper_position, portfolio_summary


def _market(price: float = 0.62, market_id: str = "m-paper-1") -> Market:
    return Market(
        market_id=market_id,
        question="Will the test market resolve yes?",
        condition_id="0xpaper",
        slug="test-market",
        outcomes=["Yes", "No"],
        outcome_prices=[price, 1 - price],
        clob_token_ids=["yes-token", "no-token"],
        volume=100_000,
        liquidity=25_000,
        active=True,
        closed=False,
    )


def _score(total: int = 88) -> ScoreBreakdown:
    return ScoreBreakdown(
        total_score=total,
        recommendation="RESEARCH_CANDIDATE",
        dimensions={"volume_liquidity": 30},
        reasoning=["High confidence simulated signal"],
    )


def test_paper_trade_opens_virtual_position_with_risk_cap(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    config = PaperTradingConfig(bankroll=1_000, max_risk_per_trade_pct=0.02, max_total_exposure_pct=0.20)

    position = maybe_open_paper_position(conn, _market(price=0.62), _score(90), config=config)
    conn.commit()

    assert position is not None
    assert position.market_id == "m-paper-1"
    assert position.side == "YES"
    assert position.entry_price == 0.62
    assert position.stake == 20.0
    assert round(position.shares, 4) == round(20.0 / 0.62, 4)
    assert position.status == "OPEN"

    stored = conn.execute("SELECT stake, entry_price, status FROM paper_positions").fetchone()
    assert stored == (20.0, 0.62, "OPEN")


def test_paper_trade_does_not_duplicate_open_position(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    config = PaperTradingConfig(bankroll=1_000)

    first = maybe_open_paper_position(conn, _market(), _score(), config=config)
    second = maybe_open_paper_position(conn, _market(), _score(), config=config)

    assert first is not None
    assert second is None
    count = conn.execute("SELECT COUNT(*) FROM paper_positions WHERE market_id = ?", ("m-paper-1",)).fetchone()[0]
    assert count == 1


def test_paper_trade_respects_score_and_total_exposure_caps(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    config = PaperTradingConfig(bankroll=100, min_score=80, max_risk_per_trade_pct=0.10, max_total_exposure_pct=0.10)

    low_score = maybe_open_paper_position(conn, _market(), _score(70), config=config)
    first = maybe_open_paper_position(conn, _market(), _score(90), config=config)

    second_market = _market(market_id="m-paper-2")
    second = maybe_open_paper_position(conn, second_market, _score(90), config=config)

    assert low_score is None
    assert first is not None
    assert second is None
    summary = portfolio_summary(conn, bankroll=100)
    assert summary["open_positions"] == 1
    assert summary["open_exposure"] == 10.0
    assert summary["available_cash"] == 90.0


def test_open_position_debits_persistent_cash_and_writes_ledger(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    config = PaperTradingConfig(bankroll=100, max_risk_per_trade_pct=0.10, max_total_exposure_pct=0.50)

    maybe_open_paper_position(conn, _market(market_id="m-cash-1"), _score(), config=config)
    maybe_open_paper_position(conn, _market(market_id="m-cash-2"), _score(), config=config)

    summary = portfolio_summary(conn, bankroll=100)
    assert summary["bankroll"] == 100.0
    assert summary["available_cash"] == 80.0
    assert summary["open_exposure"] == 20.0

    ledger_rows = conn.execute("SELECT event_type, market_id, amount FROM paper_ledger ORDER BY id").fetchall()
    assert ledger_rows == [
        ("OPEN", "m-cash-1", -10.0),
        ("OPEN", "m-cash-2", -10.0),
    ]


def test_close_position_credits_payout_and_records_win_loss_trace(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)
    config = PaperTradingConfig(bankroll=100, max_risk_per_trade_pct=0.10, max_total_exposure_pct=0.50)

    maybe_open_paper_position(conn, _market(price=0.25, market_id="m-win"), _score(), config=config)
    maybe_open_paper_position(conn, _market(price=0.50, market_id="m-loss"), _score(), config=config)

    win = close_paper_position(conn, "m-win", winning_side="YES")
    loss = close_paper_position(conn, "m-loss", winning_side="NO")

    assert win is not None
    assert win["outcome"] == "WIN"
    assert win["winning_side"] == "YES"
    assert win["payout"] == 40.0
    assert win["pnl"] == 30.0
    assert loss is not None
    assert loss["outcome"] == "LOSS"
    assert loss["winning_side"] == "NO"
    assert loss["payout"] == 0.0
    assert loss["pnl"] == -10.0

    summary = portfolio_summary(conn, bankroll=100)
    assert summary["available_cash"] == 120.0
    assert summary["realized_pnl"] == 20.0

    ledger_rows = conn.execute("SELECT event_type, market_id, amount, cash_balance_after FROM paper_ledger ORDER BY id").fetchall()
    assert ledger_rows == [
        ("OPEN", "m-win", -10.0, 90.0),
        ("OPEN", "m-loss", -10.0, 80.0),
        ("CLOSE_WIN", "m-win", 40.0, 120.0),
        ("CLOSE_LOSS", "m-loss", 0.0, 120.0),
    ]
