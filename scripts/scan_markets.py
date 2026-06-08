#!/usr/bin/env python3
"""Run a read-only Polymarket scan and write a Markdown report."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from polymarket_research.client import PolymarketClient
from polymarket_research.db import connect, init_db
from polymarket_research.reporting import insert_signal, upsert_market, write_scan_report
from polymarket_research.scorer import score_market


async def scan(limit: int, db_path: Path, report_dir: Path, threshold: int) -> Path:
    client = PolymarketClient()
    markets = await client.markets(limit=limit)

    conn = connect(db_path)
    init_db(conn)

    scored = []
    for market in markets:
        spread = None
        if market.clob_token_ids:
            spread = await client.spread(market.clob_token_ids[0])
        score = score_market(market, spread=spread)
        upsert_market(conn, market)
        if score.total_score >= threshold:
            insert_signal(conn, market, score)
        scored.append((market, score))
    conn.commit()

    return write_scan_report(report_dir, scored, threshold=threshold)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Polymarket market scanner")
    parser.add_argument("--limit", type=int, default=10, help="Number of active markets to scan")
    parser.add_argument("--threshold", type=int, default=65, help="Minimum score for a signal")
    parser.add_argument("--db", type=Path, default=Path("data/hermes_polymarket.db"))
    parser.add_argument("--reports", type=Path, default=Path("outputs/reports"))
    args = parser.parse_args()

    report = asyncio.run(scan(args.limit, args.db, args.reports, args.threshold))
    print(report)


if __name__ == "__main__":
    main()
