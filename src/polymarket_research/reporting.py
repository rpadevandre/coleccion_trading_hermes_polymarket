"""Markdown report generation for Polymarket research scans."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import sqlite3

from .models import Market, ScoreBreakdown


def upsert_market(conn: sqlite3.Connection, market: Market) -> None:
    conn.execute(
        """
        INSERT INTO markets (
            market_id, question, condition_id, slug, outcomes_json,
            outcome_prices_json, clob_token_ids_json, volume, liquidity,
            active, closed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(market_id) DO UPDATE SET
            question=excluded.question,
            condition_id=excluded.condition_id,
            slug=excluded.slug,
            outcomes_json=excluded.outcomes_json,
            outcome_prices_json=excluded.outcome_prices_json,
            clob_token_ids_json=excluded.clob_token_ids_json,
            volume=excluded.volume,
            liquidity=excluded.liquidity,
            active=excluded.active,
            closed=excluded.closed,
            last_seen_at=CURRENT_TIMESTAMP
        """,
        market.to_db_tuple(),
    )


def insert_signal(conn: sqlite3.Connection, market: Market, score: ScoreBreakdown) -> None:
    conn.execute(
        """
        INSERT INTO signals (
            market_id, total_score, recommendation, dimensions_json, reasoning_json
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (
            market.market_id,
            score.total_score,
            score.recommendation,
            json.dumps(score.dimensions, ensure_ascii=False),
            json.dumps(score.reasoning, ensure_ascii=False),
        ),
    )


def write_scan_report(
    report_dir: str | Path,
    scored_markets: list[tuple[Market, ScoreBreakdown]],
    *,
    threshold: int = 65,
) -> Path:
    report_root = Path(report_dir)
    report_root.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    path = report_root / f"SCAN_{now:%Y-%m-%d_%H%M%S}_UTC.md"

    lines = [
        f"# Polymarket scan — {now:%Y-%m-%d %H:%M:%S UTC}",
        "",
        "Modo: read-only research. No se ejecuta ninguna operación.",
        "",
        f"Umbral de señal: {threshold}/100",
        "",
        "## Señales sobre umbral",
        "",
    ]
    signals = [(m, s) for m, s in scored_markets if s.total_score >= threshold]
    if not signals:
        lines.append("No hubo señales sobre umbral en este escaneo.")
    for market, score in signals:
        lines += [
            f"### {market.question}",
            "",
            f"- Recomendación: `{score.recommendation}`",
            f"- Score: `{score.total_score}/100`",
            f"- Slug: `{market.slug}`",
            f"- Volume: `${market.volume:,.0f}`",
            f"- Liquidity: `${market.liquidity:,.0f}`",
            f"- Prices: `{market.outcome_prices}`",
            f"- Dimensions: `{score.dimensions}`",
            "- Razonamiento:",
        ]
        lines += [f"  - {reason}" for reason in score.reasoning]
        lines.append("")

    lines += ["## Todos los mercados revisados", ""]
    for market, score in scored_markets:
        lines.append(f"- `{score.total_score:03d}` `{score.recommendation}` — {market.question}")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path
