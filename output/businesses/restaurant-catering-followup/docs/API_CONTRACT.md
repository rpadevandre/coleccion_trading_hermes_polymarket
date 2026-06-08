# API Contract

## MVP endpoints

- `POST /api/intake` — create inbound item.
- `GET /api/items` — list work items.
- `GET /api/items/{id}` — item detail.
- `POST /api/items/{id}/classify` — run/refresh AI classification.
- `POST /api/items/{id}/review` — human approval/rejection/edit decision.
- `GET /api/metrics` — operational metrics.
- `GET /api/audit` — audit events.

## Security notes

All endpoints except public intake require authentication. Public intake requires rate limits, validation and abuse detection.
