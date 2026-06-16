# AION Cash-Out Protocol

## Goal

Define how Andre can ask AION to reduce or exit Polymarket exposure without relying on a vague “sell everything” command.

## Cash-Out Commands Supported

Future natural-language commands should map to structured params:

- “cash out todo” → `percent: 100`
- “cash out 50%” → `percent: 50`
- “saca 20 dólares” → `amount_pusd: 20`
- “sal de este mercado” → `market_slug: <slug>, percent: 100`
- “apaga y cash out conservador” → `mode: CASH_OUT, urgency: conservative`

## Required Steps

1. Switch mode to `CASH_OUT`.
2. Append event: `cash_out_requested`.
3. Cancel resting open orders for targeted scope.
4. Fetch current positions.
5. Fetch orderbook/liquidity.
6. Estimate slippage and likely proceeds.
7. Choose liquidation plan:
   - conservative: limit sells near fair bid, may take longer.
   - normal: limit/IOC with moderate slippage.
   - urgent: more aggressive, still bounded by max slippage unless Andre overrides.
8. Execute in PAPER_ONLY simulation or live adapter depending on approved mode.
9. Append every action/fill/failure to `ledger/events.jsonl`.
10. Send Telegram summary.

## Fail-Closed Conditions

Do not liquidate blindly if:

- current positions cannot be fetched,
- orderbook cannot be fetched,
- slippage estimate is unavailable,
- spread is above policy,
- market resolution is ambiguous,
- reconciliation is unhealthy,
- audit log cannot be written.

In those cases, report the blocker and preserve capital/state rather than pretending cash-out happened.

## Output Report

A cash-out report should include:

- requested amount/percent/market,
- positions before,
- open orders canceled,
- estimated proceeds,
- realized proceeds if live/paper fill occurred,
- remaining exposure,
- failures/partials,
- next recommended action.
