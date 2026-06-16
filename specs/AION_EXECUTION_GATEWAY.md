# AION Execution Gateway Spec

## Purpose

The AION Execution Gateway is the mandatory layer between AION's reasoning and any Polymarket order path.

It exists so AION can be useful/autonomous **inside a sandbox** while Andre retains the real controls:

- mode: `PAPER_ONLY`, `ON`, `OFF`, `CASH_OUT`
- capital budget
- max order size
- max exposure
- cash-out instruction
- permission to ever touch live execution

## Non-negotiable Rule

AION must never send raw live orders directly from a chat/reasoning step. It must produce a staged intent and pass through policy validation.

```text
AION signal → staged intent → policy checks → paper/live adapter → audit log
```

## Inputs

- `config/AION_POLYMARKET_CONTROL.yaml`
- current market/orderbook/liquidity data
- current paper/live positions
- active staged intents
- risk policy
- Andre commands from Telegram/session

## Outputs

- accepted/rejected staged intents
- paper trades
- optional live order requests in future phase
- append-only audit events in `ledger/events.jsonl`
- Markdown reports under `reports/`

## Modes

### PAPER_ONLY

Default. Allow research, scoring, simulated orders, backtests, and reports. Block live order adapters.

### ON

Only valid after live pilot approval. Allow orders if all checks pass:

- live execution enabled
- wallet/env configured outside repo
- capital budget > 0
- max order > 0
- total exposure after order <= max total exposure
- market exposure after order <= max market exposure
- liquidity >= minimum
- slippage <= maximum
- reconciliation healthy

### OFF

Block new entries. Cancel open resting orders if live mode exists and cancel-all is safe. Keep monitoring/reconciliation.

### CASH_OUT

Block new entries. Cancel open orders. Evaluate exits. Execute/propose liquidation based on cash-out params and current permission level.

## Staged Intent Schema

```json
{
  "intent_id": "uuid",
  "created_at": "iso8601",
  "mode_seen": "PAPER_ONLY",
  "market_slug": "example-market",
  "condition_id": "0x...",
  "outcome": "YES",
  "side": "BUY",
  "order_type": "LIMIT",
  "quote_amount_pusd": 5.0,
  "limit_price": 0.42,
  "thesis": "why this edge may exist",
  "evidence": ["source 1", "source 2"],
  "risks": ["liquidity", "resolution ambiguity"],
  "score": 72,
  "policy_status": "PENDING"
}
```

## Policy Checks

1. Mode check.
2. Budget check.
3. Per-order limit.
4. Total exposure limit.
5. Market/event exposure limit.
6. Category/slug allow/blocklist.
7. Liquidity minimum.
8. Spread/slippage maximum.
9. Duplicate position prevention.
10. Reconciliation health.
11. Credential isolation check for live mode.
12. Audit event append success.

If audit logging fails, execution must fail closed.

## NautilusTrader Role

NautilusTrader should be introduced first for backtesting and market data modeling, later for live execution/reconciliation.

Do not use Nautilus example tester strategies as production bots.

## OpenAlice Pattern Role

Use OpenAlice-like governance patterns, not direct code reuse:

- staged changes,
- guard pipeline,
- local state,
- audit trail,
- explicit control states.

## Verification Checklist

Before any live pilot:

- [ ] PAPER_ONLY reports work.
- [ ] Paper ledger has at least several weeks of data.
- [ ] Control state is read correctly.
- [ ] OFF blocks new intents.
- [ ] CASH_OUT simulation works.
- [ ] Risk policy rejects over-budget orders.
- [ ] Audit log is append-only.
- [ ] Secrets are absent from repo.
- [ ] Reconciliation failure blocks new entries.
