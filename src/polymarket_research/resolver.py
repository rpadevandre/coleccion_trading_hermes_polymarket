"""Resolve paper positions when public market outcomes are known."""

from __future__ import annotations

from collections.abc import Mapping
import sqlite3

from .models import Market
from .paper import close_paper_position


def infer_winning_side(market: Market) -> str | None:
    """Infer binary YES/NO winner from a closed market's final prices.

    Conservative by design: returns None unless the market is closed and final
    prices are effectively binary. This avoids inventing outcomes for ambiguous
    or still-trading markets.
    """

    if not market.closed:
        return None
    if len(market.outcome_prices) < 2:
        return None

    yes_price = float(market.outcome_prices[0])
    no_price = float(market.outcome_prices[1])
    if yes_price >= 0.99 and no_price <= 0.01:
        return "YES"
    if no_price >= 0.99 and yes_price <= 0.01:
        return "NO"
    return None


def open_paper_markets(conn: sqlite3.Connection) -> list[dict[str, str]]:
    rows = conn.execute(
        """
        SELECT DISTINCT p.market_id, m.slug
        FROM paper_positions p
        JOIN markets m ON m.market_id = p.market_id
        WHERE p.status = 'OPEN'
        ORDER BY p.opened_at ASC
        """
    ).fetchall()
    return [{"market_id": str(row[0]), "slug": str(row[1] or "")} for row in rows]


def resolve_closed_paper_positions(
    conn: sqlite3.Connection,
    markets_by_id: Mapping[str, Market],
) -> list[dict[str, float | str]]:
    """Close open paper positions when supplied markets have clear winners."""

    closed: list[dict[str, float | str]] = []
    for item in open_paper_markets(conn):
        market_id = item["market_id"]
        market = markets_by_id.get(market_id)
        if market is None:
            continue
        winning_side = infer_winning_side(market)
        if winning_side is None:
            continue
        result = close_paper_position(conn, market_id, winning_side=winning_side)
        if result is not None:
            result["winning_side"] = winning_side
            closed.append(result)
    return closed
