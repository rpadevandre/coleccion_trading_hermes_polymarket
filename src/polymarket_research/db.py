"""SQLite persistence for Polymarket research signals."""

from __future__ import annotations

from pathlib import Path
import sqlite3


def connect(db_path: str | Path) -> sqlite3.Connection:
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS markets (
            market_id TEXT PRIMARY KEY,
            question TEXT NOT NULL,
            condition_id TEXT,
            slug TEXT,
            outcomes_json TEXT NOT NULL,
            outcome_prices_json TEXT NOT NULL,
            clob_token_ids_json TEXT NOT NULL,
            volume REAL NOT NULL DEFAULT 0,
            liquidity REAL NOT NULL DEFAULT 0,
            active INTEGER NOT NULL DEFAULT 1,
            closed INTEGER NOT NULL DEFAULT 0,
            first_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            market_id TEXT NOT NULL,
            total_score INTEGER NOT NULL,
            recommendation TEXT NOT NULL,
            dimensions_json TEXT NOT NULL,
            reasoning_json TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL DEFAULT 'PENDING_REVIEW',
            FOREIGN KEY (market_id) REFERENCES markets(market_id)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS wallet_profiles (
            address TEXT PRIMARY KEY,
            label TEXT,
            notes TEXT,
            last_checked_at TEXT
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS paper_positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            market_id TEXT NOT NULL,
            side TEXT NOT NULL,
            entry_price REAL NOT NULL,
            stake REAL NOT NULL,
            shares REAL NOT NULL,
            score INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'OPEN',
            opened_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            closed_at TEXT,
            exit_price REAL,
            pnl REAL,
            FOREIGN KEY (market_id) REFERENCES markets(market_id)
        )
        """
    )
    conn.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS idx_paper_positions_one_open_per_market
        ON paper_positions(market_id)
        WHERE status = 'OPEN'
        """
    )
    conn.commit()
