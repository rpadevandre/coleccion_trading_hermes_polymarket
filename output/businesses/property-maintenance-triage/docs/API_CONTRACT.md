# API Contract — Property Maintenance Triage

Internal skeleton only. No deployment, no real tenant data, no production vendor integrations.

## API Style

- Base path: `/api/v1`
- Auth: property manager users via session/JWT; tenant intake supports magic-link/demo token.
- Tenant scope: every record belongs to `portfolio_id` and optionally `property_id` / `unit_id`.
- Data rule: prototype uses synthetic tenant/unit data only.

## Core Endpoints

### Portfolio Setup

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/portfolios` | Create a demo landlord/property manager workspace. |
| `GET` | `/portfolios/{portfolio_id}` | Load properties, vendor rules and escalation settings. |
| `PATCH` | `/portfolios/{portfolio_id}` | Update emergency definitions, office hours and routing preferences. |

### Tenant Intake

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/requests` | Create maintenance request from tenant form/SMS-style intake. |
| `POST` | `/requests/{request_id}/messages` | Add tenant, manager or vendor message. |
| `POST` | `/requests/{request_id}/attachments` | Attach demo photo/document metadata. |
| `GET` | `/requests/{request_id}` | Load request, triage result and audit trail. |

### Triage and Work Orders

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/requests/{request_id}/triage` | Classify category, urgency, missing info and suggested vendor route. |
| `PATCH` | `/requests/{request_id}/triage` | Human override of urgency/category/vendor route. |
| `POST` | `/requests/{request_id}/work-order` | Convert approved request into work-order draft. |
| `POST` | `/requests/{request_id}/vendor-draft` | Draft vendor dispatch message with tenant-safe summary. |

### Admin and Metrics

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/admin/metrics` | SLA risk, open emergency requests, aging, repeat issues by property. |
| `GET` | `/admin/routing-rules` | List category-to-vendor and escalation rules. |
| `POST` | `/admin/routing-rules` | Create/update routing rule. |
| `GET` | `/admin/audit-events` | Immutable log of request, triage and work-order changes. |

## Example Request

```json
{
  "request_id": "req_demo_001",
  "portfolio_id": "por_demo_001",
  "property_id": "prop_demo_duplex_01",
  "tenant_message": "water dripping from ceiling near bathroom",
  "triage": {
    "category": "plumbing_leak",
    "urgency": "emergency",
    "confidence": 0.86,
    "missing_info": ["photo", "active leak status", "shutoff attempted"]
  }
}
```

## Error Codes

- `400_INVALID_INTAKE` — message too short or missing unit reference.
- `401_UNAUTHENTICATED` — manager/admin session missing.
- `403_SCOPE_MISMATCH` — attempted access outside portfolio.
- `409_ALREADY_CONVERTED` — duplicate work-order conversion.
- `422_REAL_TENANT_DATA_NOT_ALLOWED` — demo environment received real tenant PII.
