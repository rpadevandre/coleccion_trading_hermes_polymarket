# API Contract

## MVP endpoints

- `POST /api/intake` — create inbound item.
- `GET /api/items` — list work items.
- `GET /api/items/{id}` — item detail.
- `POST /api/items/{id}/classify` — run/refresh AI classification.
- `POST /api/items/{id}/review` — human approval/rejection/edit decision.
- `PATCH /api/items/{id}/status` — update workflow state.
- `GET /api/metrics` — operational metrics.
- `GET /api/audit` — audit events.

## Security notes

Public intake must be rate-limited and validated. All operational/admin endpoints require authentication, authorization and audit logs.
