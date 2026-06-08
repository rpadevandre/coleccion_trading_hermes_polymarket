#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
fi

if ! .venv/bin/python - <<'PY' >/dev/null 2>&1
import polymarket_research  # noqa: F401
PY
then
  .venv/bin/python -m pip install -q -e '.[dev]'
fi

PAPER_BANKROLL="${POLYMARKET_PAPER_BANKROLL:-1000}"
OUTPUT="$(.venv/bin/python scripts/update_paper_positions.py --bankroll "$PAPER_BANKROLL")"

# Watchdog pattern: stay silent unless something actually closed.
if ! grep -q 'Positions auto-closed: `0`' <<<"$OUTPUT"; then
  printf '%s\n' "$OUTPUT"
fi
