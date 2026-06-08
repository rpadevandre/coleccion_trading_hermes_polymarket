# API Contract — Dental Insurance Checklist Assistant

Internal skeleton only. No real payer credentials, no PHI, no production deployment.

## API Style

- Base path: `/api/v1`
- Auth: session/JWT for office users; service token for internal workers.
- Tenant scope: every request is scoped by `practice_id`.
- Data rule: use synthetic/demo patient data until a compliant environment exists.

## Core Endpoints

### Practices

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/practices` | Create a demo dental practice workspace. |
| `GET` | `/practices/{practice_id}` | Load practice settings, checklist defaults and integrations status. |
| `PATCH` | `/practices/{practice_id}` | Update office hours, payer list, disclaimers and verification SOP. |

### Patients and Visits

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/visits` | Create a pre-visit verification case. |
| `GET` | `/visits?status=&date=` | List verification queue. |
| `GET` | `/visits/{visit_id}` | Load visit, checklist, notes and audit trail. |
| `PATCH` | `/visits/{visit_id}` | Update appointment, payer, plan or status fields. |

### Checklist Workflow

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/visits/{visit_id}/checklist/generate` | Generate payer-specific checklist from appointment type and plan metadata. |
| `PATCH` | `/checklist-items/{item_id}` | Mark item complete, blocked or needs follow-up. |
| `POST` | `/visits/{visit_id}/notes/draft` | Draft PMS-ready benefit notes and patient-facing summary. |
| `POST` | `/visits/{visit_id}/exceptions` | Capture missing information, conflicting eligibility, inactive coverage or coordination-of-benefits issue. |

### Admin and Reporting

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/admin/metrics` | Queue aging, completed checks, blocked checks, time saved estimate. |
| `GET` | `/admin/audit-events` | Immutable event log for each verification action. |
| `POST` | `/admin/templates` | Create reusable verification scripts, payer prompts and disclaimers. |

## Example Objects

```json
{
  "visit_id": "vis_demo_001",
  "practice_id": "pra_demo_001",
  "appointment_type": "crown prep",
  "payer_name": "Demo Dental Plan",
  "status": "needs_verification",
  "checklist_summary": {
    "required_items": 9,
    "completed_items": 4,
    "blocked_items": 1
  }
}
```

## Error Codes

- `400_INVALID_FIELD` — unsupported appointment or missing plan metadata.
- `401_UNAUTHENTICATED` — no valid user session.
- `403_SCOPE_MISMATCH` — user tried to access another practice.
- `409_STATUS_CONFLICT` — stale checklist update.
- `422_PHI_NOT_ALLOWED_IN_DEMO` — demo environment received real patient identifiers.
