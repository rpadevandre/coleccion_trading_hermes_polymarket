from polymarket_research.models import Market
from polymarket_research.scorer import score_market


def test_market_parses_double_encoded_polymarket_fields():
    raw = {
        "id": "m1",
        "question": "Will X happen?",
        "conditionId": "0xabc",
        "slug": "will-x-happen",
        "outcomes": '["Yes", "No"]',
        "outcomePrices": '["0.64", "0.36"]',
        "clobTokenIds": '["yes-token", "no-token"]',
        "volume": "25000",
        "liquidity": "12000",
        "active": True,
        "closed": False,
    }

    market = Market.from_gamma(raw)

    assert market.market_id == "m1"
    assert market.question == "Will X happen?"
    assert market.outcomes == ["Yes", "No"]
    assert market.outcome_prices == [0.64, 0.36]
    assert market.clob_token_ids == ["yes-token", "no-token"]
    assert market.volume == 25000.0
    assert market.liquidity == 12000.0


def test_score_market_is_deterministic_and_explainable():
    market = Market(
        market_id="m1",
        question="Will X happen?",
        condition_id="0xabc",
        slug="will-x-happen",
        outcomes=["Yes", "No"],
        outcome_prices=[0.62, 0.38],
        clob_token_ids=["yes-token", "no-token"],
        volume=50000.0,
        liquidity=20000.0,
        active=True,
        closed=False,
    )

    first = score_market(market, spread=0.02)
    second = score_market(market, spread=0.02)

    assert first == second
    assert first.total_score >= 65
    assert first.recommendation in {"WATCH", "RESEARCH_CANDIDATE"}
    assert set(first.dimensions) == {
        "volume_liquidity",
        "spread_risk",
        "price_sanity",
        "market_activity",
        "source_reliability",
    }
    assert first.reasoning
