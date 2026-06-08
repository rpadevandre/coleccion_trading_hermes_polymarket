#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
fi

if ! .venv/bin/python - <<'PY' >/dev/null 2>&1
import pytest  # noqa: F401
import polymarket_research  # noqa: F401
PY
then
  .venv/bin/python -m pip install -e '.[dev]' >/dev/null
fi

LIMIT="${POLYMARKET_SCAN_LIMIT:-10}"
THRESHOLD="${POLYMARKET_SIGNAL_THRESHOLD:-65}"
REPORT_PATH="$(.venv/bin/python scripts/scan_markets.py --limit "$LIMIT" --threshold "$THRESHOLD")"

cat <<EOF
# Polymarket Research Scan

Repo: rpadevandre/coleccion_trading_hermes_polymarket  
Modo: read-only research — no trades, no wallets, no dinero real.

Reporte generado: $REPORT_PATH

---
EOF

cat "$REPORT_PATH"
