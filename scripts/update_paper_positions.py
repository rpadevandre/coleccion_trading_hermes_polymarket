#!/usr/bin/env python3
"""Auto-resolve fictional paper positions when markets have clear outcomes.

This script is paper-only. It reads open virtual positions, fetches their public
Gamma market by slug, infers a binary winner only when final prices are clear,
and closes the virtual position in SQLite.
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from polymarket_research.client import PolymarketClient
from polymarket_research.db import connect, init_db
from polymarket_research.paper import performance_summary
from polymarket_research.resolver import open_paper_markets, resolve_closed_paper_positions


def render_summary(summary: dict[str, float | int]) -> str:
    return "\n".join(
        [
            "# Polymarket Paper Trading Performance",
            "",
            "Modo: dinero ficticio. No wallets, no órdenes reales.",
            "",
            "## Portfolio ficticio",
            "",
            f"- Bankroll: `${summary['bankroll']:,.2f}`",
            f"- Posiciones abiertas: `{summary['open_positions']}`",
            f"- Exposición abierta: `${summary['open_exposure']:,.2f}`",
            f"- Cash disponible: `${summary['available_cash']:,.2f}`",
            "",
            "## Performance cerrada",
            "",
            f"- Posiciones cerradas: `{summary['closed_positions']}`",
            f"- Wins: `{summary['wins']}`",
            f"- Losses: `{summary['losses']}`",
            f"- P&L realizado: `${summary['realized_pnl']:,.2f}`",
            f"- Stake cerrado: `${summary['closed_stake']:,.2f}`",
            f"- ROI sobre stake cerrado: `{summary['roi_pct']:,.2f}%`",
            f"- Win rate: `{summary['win_rate_pct']:,.2f}%`",
            "",
        ]
    )


async def update(db_path: Path, bankroll: float) -> str:
    conn = connect(db_path)
    init_db(conn)
    open_items = open_paper_markets(conn)

    client = PolymarketClient()
    markets_by_id = {}
    for item in open_items:
        slug = item.get("slug") or ""
        if not slug:
            continue
        market = await client.market_by_slug(slug)
        if market is not None:
            # Keep local market_id as source of truth because Gamma id formats can vary.
            markets_by_id[item["market_id"]] = market

    closed = resolve_closed_paper_positions(conn, markets_by_id)
    conn.commit()

    lines = [
        "# Polymarket Paper Position Update",
        "",
        "Modo: dinero ficticio. No wallets, no órdenes reales.",
        "",
        f"Open positions checked: `{len(open_items)}`",
        f"Positions auto-closed: `{len(closed)}`",
        "",
    ]
    if closed:
        lines += ["## Posiciones cerradas", ""]
        for item in closed:
            lines.append(
                f"- `{item['market_id']}` winner `{item['winning_side']}` exit `{item['exit_price']}` pnl `${item['pnl']:,.2f}`"
            )
        lines.append("")
    else:
        lines += ["No había posiciones con resolución clara todavía.", ""]

    lines.append(render_summary(performance_summary(conn, bankroll=bankroll)))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Auto-update paper positions from public Polymarket outcomes")
    parser.add_argument("--db", type=Path, default=Path("data/hermes_polymarket.db"))
    parser.add_argument("--bankroll", type=float, default=1_000.0)
    args = parser.parse_args()
    print(asyncio.run(update(args.db, args.bankroll)))


if __name__ == "__main__":
    main()
