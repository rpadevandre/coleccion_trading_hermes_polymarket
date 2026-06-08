"""Markdown report generation for Polymarket research scans."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import sqlite3

from .models import Market, ScoreBreakdown
from .paper import PaperPosition


def upsert_market(conn: sqlite3.Connection, market: Market) -> None:
    conn.execute(
        """
        INSERT INTO markets (
            market_id, question, condition_id, slug, outcomes_json,
            outcome_prices_json, clob_token_ids_json, volume, liquidity,
            active, closed, end_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            end_date=excluded.end_date,
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
    paper_positions: list[PaperPosition] | None = None,
    paper_summary: dict[str, float | int] | None = None,
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
            f"- End date: `{market.end_date or 'unknown'}`",
            f"- Dimensions: `{score.dimensions}`",
            "- Razonamiento:",
        ]
        lines += [f"  - {reason}" for reason in score.reasoning]
        lines.append("")

    if paper_summary is not None:
        lines += [
            "## Paper trading interno",
            "",
            "Modo: dinero ficticio. No hay wallets ni órdenes reales.",
            "",
            f"- Bankroll ficticio: `${paper_summary['bankroll']:,.2f}`",
            f"- Posiciones abiertas: `{paper_summary['open_positions']}`",
            f"- Exposición abierta: `${paper_summary['open_exposure']:,.2f}`",
            f"- Cash ficticio disponible: `${paper_summary['available_cash']:,.2f}`",
            "",
        ]
        if "closed_positions" in paper_summary:
            lines += [
                "### Performance cerrada",
                "",
                f"- Posiciones cerradas: `{paper_summary['closed_positions']}`",
                f"- Wins: `{paper_summary['wins']}`",
                f"- Losses: `{paper_summary['losses']}`",
                f"- P&L realizado: `${paper_summary['realized_pnl']:,.2f}`",
                f"- ROI sobre stake cerrado: `{paper_summary['roi_pct']:,.2f}%`",
                f"- Win rate: `{paper_summary['win_rate_pct']:,.2f}%`",
                "",
            ]
        paper_positions = paper_positions or []
        if paper_positions:
            lines += ["### Nuevas posiciones ficticias abiertas en este scan", ""]
            for position in paper_positions:
                lines.append(
                    f"- `{position.side}` `{position.market_id}` — stake `${position.stake:,.2f}` "
                    f"at `{position.entry_price:.4f}` ({position.shares:.4f} shares), score `{position.score}`"
                )
            lines.append("")
        else:
            lines += ["No se abrió ninguna posición ficticia nueva en este scan.", ""]

    lines += ["## Todos los mercados revisados", ""]
    for market, score in scored_markets:
        lines.append(f"- `{score.total_score:03d}` `{score.recommendation}` — {market.question}")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path
