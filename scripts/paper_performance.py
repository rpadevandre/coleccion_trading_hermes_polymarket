#!/usr/bin/env python3
"""Inspect and update paper-trading performance.

This script is intentionally paper-only. It can summarize fictional positions and
manually close a position when a market resolution is known.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.paper import close_paper_position, performance_summary


def render_summary(summary: dict[str, float | int]) -> str:
    lines = [
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
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Paper-trading performance helper")
    parser.add_argument("--db", type=Path, default=Path("data/hermes_polymarket.db"))
    parser.add_argument("--bankroll", type=float, default=1_000.0)
    parser.add_argument("--close-market", help="Market ID to manually close in paper mode")
    parser.add_argument("--winning-side", choices=["YES", "NO", "yes", "no"], help="Resolved winning side for --close-market")
    args = parser.parse_args()

    conn = connect(args.db)
    init_db(conn)

    if args.close_market:
        if not args.winning_side:
            raise SystemExit("--winning-side is required when using --close-market")
        closed = close_paper_position(conn, args.close_market, winning_side=args.winning_side)
        conn.commit()
        if closed is None:
            print(f"No open paper position found for market {args.close_market}")
        else:
            print(
                f"Closed {closed['market_id']} with exit={closed['exit_price']} pnl=${closed['pnl']:,.2f}"
            )
            print("")

    print(render_summary(performance_summary(conn, bankroll=args.bankroll)))


if __name__ == "__main__":
    main()
