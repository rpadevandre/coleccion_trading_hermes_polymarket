"""Deterministic opportunity scoring for read-only Polymarket research.

The weights are deliberately simple and explainable for the MVP. They are not
financial advice and must be recalibrated during paper trading.
"""

from __future__ import annotations

from .models import Market, ScoreBreakdown


def _clamp(value: float, lower: int = 0, upper: int = 100) -> int:
    return max(lower, min(upper, round(value)))


def score_market(market: Market, spread: float | None = None) -> ScoreBreakdown:
    """Return an explainable 0-100 opportunity score.

    Dimensions are weighted to sum to 100:
    - volume_liquidity: 30
    - spread_risk: 20
    - price_sanity: 20
    - market_activity: 15
    - source_reliability: 15
    """
    reasoning: list[str] = []

    # Formula propia MVP: saturates after moderate liquidity/volume.
    volume_component = min(market.volume / 50_000, 1.0) * 15
    liquidity_component = min(market.liquidity / 20_000, 1.0) * 15
    volume_liquidity = _clamp(volume_component + liquidity_component, 0, 30)
    reasoning.append(f"Volume/liquidity score {volume_liquidity}/30 based on ${market.volume:,.0f} volume and ${market.liquidity:,.0f} liquidity.")

    if spread is None:
        spread_risk = 10
        reasoning.append("Spread unavailable; assigned neutral risk score 10/20.")
    elif spread <= 0.02:
        spread_risk = 20
        reasoning.append(f"Tight spread {spread:.3f}; low execution-friction risk.")
    elif spread <= 0.05:
        spread_risk = 14
        reasoning.append(f"Moderate spread {spread:.3f}; acceptable friction.")
    else:
        spread_risk = 6
        reasoning.append(f"Wide spread {spread:.3f}; high friction risk.")

    prices = [p for p in market.outcome_prices if 0 <= p <= 1]
    if len(prices) >= 2 and abs(sum(prices[:2]) - 1.0) <= 0.08:
        max_price = max(prices[:2])
        # Avoid markets too close to certainty unless later edge model says otherwise.
        price_sanity = 20 if 0.15 <= max_price <= 0.85 else 10
    else:
        price_sanity = 5
    reasoning.append(f"Price sanity score {price_sanity}/20 from outcome prices {market.outcome_prices}.")

    market_activity = 15 if market.active and not market.closed else 0
    reasoning.append("Market is active/open." if market_activity else "Market is inactive or closed.")

    source_reliability = 15 if market.condition_id and market.clob_token_ids else 7
    reasoning.append(
        "Market has conditionId and CLOB token IDs."
        if source_reliability == 15
        else "Market is missing conditionId or CLOB token IDs."
    )

    dimensions = {
        "volume_liquidity": volume_liquidity,
        "spread_risk": spread_risk,
        "price_sanity": price_sanity,
        "market_activity": market_activity,
        "source_reliability": source_reliability,
    }
    total = sum(dimensions.values())
    if total >= 80:
        recommendation = "RESEARCH_CANDIDATE"
    elif total >= 65:
        recommendation = "WATCH"
    else:
        recommendation = "SKIP"

    return ScoreBreakdown(total_score=total, recommendation=recommendation, dimensions=dimensions, reasoning=reasoning)
