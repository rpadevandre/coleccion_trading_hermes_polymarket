#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install -e '.[dev]'
fi

LIMIT="${POLYMARKET_SCAN_LIMIT:-10}"
THRESHOLD="${POLYMARKET_SIGNAL_THRESHOLD:-65}"

.venv/bin/python scripts/scan_markets.py --limit "$LIMIT" --threshold "$THRESHOLD"
