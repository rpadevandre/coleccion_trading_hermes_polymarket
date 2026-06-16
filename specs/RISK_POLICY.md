# AION Polymarket Risk Policy

## Default Position

AION is paper-only until Andre explicitly authorizes a live micro-wallet pilot.

## Capital Rules

- Never exceed `capital_budget_pusd`.
- Never exceed `max_order_pusd` per order.
- Never exceed `max_market_exposure_pusd` per market/event.
- Never exceed `max_total_open_exposure_pusd` across all open positions.
- If any limit is zero, live entries are disabled.

## Market Quality Rules

Reject or flag markets with:

- insufficient liquidity,
- wide spreads,
- ambiguous resolution criteria,
- unsupported market type,
- extremely low volume,
- stale data,
- high API uncertainty/rate-limit errors.

## Execution Rules

- Market BUY must use quote quantity / pUSD notional semantics.
- Prefer limit orders for controlled entries/exits.
- No reduce-only assumption; Polymarket adapter does not support reduce-only.
- No bracket/OCO assumption; not supported by Polymarket adapter.
- No live order if audit event cannot be appended.
- No live order if reconciliation is unhealthy.

## AI Decision Rules

AION must produce:

- thesis,
- evidence,
- counterargument,
- risk list,
- score,
- proposed size,
- invalidation/cash-out conditions.

Low-confidence signals should become watchlist items, not trades.

## Human/Switch Rules

Andre controls:

- enabling live pilot,
- capital budget,
- ON/OFF,
- cash-out,
- category/market blocks.

AION may recommend changes but must not silently expand its own permissions.
