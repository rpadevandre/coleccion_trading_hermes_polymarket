#!/usr/bin/env python3
"""Run a read-only Polymarket scan and write a Markdown report."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from polymarket_research.client import PolymarketClient
from polymarket_research.db import connect, init_db
from polymarket_research.paper import PaperTradingConfig, maybe_open_paper_position, performance_summary
from polymarket_research.reporting import insert_signal, upsert_market, write_scan_report
from polymarket_research.scorer import score_market


async def scan(
    limit: int,
    db_path: Path,
    report_dir: Path,
    threshold: int,
    *,
    paper: bool = False,
    paper_bankroll: float = 1_000.0,
    paper_min_score: int = 80,
    max_hours_to_close: int | None = None,
) -> Path:
    client = PolymarketClient()
    markets = await client.markets(limit=limit, max_hours_to_close=max_hours_to_close)

    conn = connect(db_path)
    init_db(conn)

    scored = []
    paper_positions = []
    paper_config = PaperTradingConfig(bankroll=paper_bankroll, min_score=paper_min_score)
    for market in markets:
        spread = None
        if market.clob_token_ids:
            spread = await client.spread(market.clob_token_ids[0])
        score = score_market(market, spread=spread)
        upsert_market(conn, market)
        if score.total_score >= threshold:
            insert_signal(conn, market, score)
        if paper:
            position = maybe_open_paper_position(conn, market, score, config=paper_config)
            if position is not None:
                paper_positions.append(position)
        scored.append((market, score))
    conn.commit()

    summary = performance_summary(conn, bankroll=paper_bankroll) if paper else None
    if paper:
        conn.commit()
    return write_scan_report(
        report_dir,
        scored,
        threshold=threshold,
        paper_positions=paper_positions,
        paper_summary=summary,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Polymarket market scanner")
    parser.add_argument("--limit", type=int, default=10, help="Number of active markets to scan")
    parser.add_argument("--threshold", type=int, default=65, help="Minimum score for a signal")
    parser.add_argument("--db", type=Path, default=Path("data/hermes_polymarket.db"))
    parser.add_argument("--reports", type=Path, default=Path("outputs/reports"))
    parser.add_argument("--paper", action="store_true", help="Open fictional paper-trading positions for strong signals")
    parser.add_argument("--paper-bankroll", type=float, default=1_000.0, help="Fictional bankroll for paper trading")
    parser.add_argument("--paper-min-score", type=int, default=80, help="Minimum score required to open a paper position")
    parser.add_argument(
        "--max-hours-to-close",
        type=int,
        default=None,
        help="Only scan markets whose end date is within this many hours; useful for fast paper feedback loops",
    )
    args = parser.parse_args()

    report = asyncio.run(
        scan(
            args.limit,
            args.db,
            args.reports,
            args.threshold,
            paper=args.paper,
            paper_bankroll=args.paper_bankroll,
            paper_min_score=args.paper_min_score,
            max_hours_to_close=args.max_hours_to_close,
        )
    )
    print(report)


if __name__ == "__main__":
    main()
