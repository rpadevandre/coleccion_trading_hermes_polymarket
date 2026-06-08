from pathlib import Path

from polymarket_research.db import connect, init_db
from polymarket_research.models import Market


def test_init_db_enables_wal_and_can_store_market(tmp_path: Path):
    db_path = tmp_path / "hermes_polymarket.db"

    conn = connect(db_path)
    init_db(conn)
    journal_mode = conn.execute("PRAGMA journal_mode").fetchone()[0]

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
    conn.execute(
        """
        INSERT INTO markets (
            market_id, question, condition_id, slug, outcomes_json,
            outcome_prices_json, clob_token_ids_json, volume, liquidity,
            active, closed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        market.to_db_tuple(),
    )
    conn.commit()

    row = conn.execute("SELECT question, volume FROM markets WHERE market_id = ?", ("m1",)).fetchone()

    assert journal_mode.lower() == "wal"
    assert row == ("Will X happen?", 50000.0)
