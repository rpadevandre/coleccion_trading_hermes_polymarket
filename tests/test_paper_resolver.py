from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.models import Market, ScoreBreakdown
from polymarket_research.paper import PaperTradingConfig, maybe_open_paper_position
from polymarket_research.resolver import infer_winning_side, resolve_closed_paper_positions


def _market(market_id: str = "m-resolve", *, closed: bool = True, prices: list[float] | None = None) -> Market:
    return Market(
        market_id=market_id,
        question="Resolved paper market?",
        condition_id="0xresolve",
        slug=f"slug-{market_id}",
        outcomes=["Yes", "No"],
        outcome_prices=prices or [1.0, 0.0],
        clob_token_ids=["yes-token", "no-token"],
        volume=10_000,
        liquidity=1_000,
        active=not closed,
        closed=closed,
    )


def _score() -> ScoreBreakdown:
    return ScoreBreakdown(
        total_score=90,
        recommendation="RESEARCH_CANDIDATE",
        dimensions={"test": 1},
        reasoning=["test"],
    )


def test_infer_winning_side_from_closed_binary_prices():
    assert infer_winning_side(_market(prices=[1.0, 0.0])) == "YES"
    assert infer_winning_side(_market(prices=[0.0, 1.0])) == "NO"


def test_infer_winning_side_returns_none_for_open_or_ambiguous_market():
    assert infer_winning_side(_market(closed=False, prices=[0.7, 0.3])) is None
    assert infer_winning_side(_market(closed=True, prices=[0.55, 0.45])) is None


def test_resolve_closed_paper_positions_closes_only_resolved_markets(tmp_path: Path):
    conn = connect(tmp_path / "paper.db")
    init_db(conn)

    winner = _market("winner", closed=False, prices=[0.25, 0.75])
    loser = _market("loser", closed=False, prices=[0.5, 0.5])
    unresolved = _market("unresolved", closed=False, prices=[0.4, 0.6])

    config = PaperTradingConfig(bankroll=1_000)
    for market in [winner, loser, unresolved]:
        maybe_open_paper_position(conn, market, _score(), config=config)
    conn.commit()

    resolved = resolve_closed_paper_positions(
        conn,
        {
            "winner": _market("winner", closed=True, prices=[1.0, 0.0]),
            "loser": _market("loser", closed=True, prices=[0.0, 1.0]),
            "unresolved": _market("unresolved", closed=True, prices=[0.51, 0.49]),
        },
    )

    assert len(resolved) == 2
    assert {item["market_id"] for item in resolved} == {"winner", "loser"}

    rows = conn.execute("SELECT market_id, status, pnl FROM paper_positions ORDER BY market_id").fetchall()
    assert rows == [
        ("loser", "CLOSED", -20.0),
        ("unresolved", "OPEN", None),
        ("winner", "CLOSED", 60.0),
    ]
