from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.models import Market, ScoreBreakdown
from polymarket_research.paper import PaperTradingConfig, maybe_open_paper_position, portfolio_summary


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
