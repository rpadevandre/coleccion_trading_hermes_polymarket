# API Contract — Restaurant Catering Follow-Up Copilot

Base path: `/api/v1`

All endpoints require workspace authentication unless marked public. The MVP favors export/copy workflows and staff approval, not automatic outbound sending.

## Public lead endpoint

### `POST /leads/catering-audit-request`
Request:
```json
{
  "restaurant_name": "Main Street Deli",
  "website": "https://example-deli.com/catering",
  "contact_name": "Sam Owner",
  "email": "sam@example.com",
  "location_count": 2,
  "average_catering_order_value": 425,
  "monthly_catering_inquiries": 35,
  "current_followup_process": "spreadsheet and phone reminders",
  "consent_to_contact": true
}
```

Response `201`:
```json
{ "lead_id": "lead_123", "status": "received" }
```

## Workspace dashboard

### `GET /workspaces/{workspace_id}/dashboard`
Response:
```json
{
  "followups_due_today": 14,
  "overdue_followups": 3,
  "pipeline_value": 18450,
  "recovered_revenue_month_to_date": 3920,
  "stages": {
    "quote_pending": 12,
    "first_order": 8,
    "repeat": 21,
    "lapsed": 17
  },
  "warnings": ["4 contacts missing email", "2 drafts need menu/pricing review"]
}
```

## Import endpoints

### `POST /workspaces/{workspace_id}/imports`
Creates an import batch from CSV metadata or pasted records.

Request:
```json
{
  "source_type": "csv",
  "filename": "last-90-days-catering.csv",
  "mapping": {
    "contact_email": "Email",
    "company_name": "Company",
    "event_date": "Event Date",
    "order_value": "Total"
  }
}
```

Response `202`:
```json
{ "import_batch_id": "imp_123", "status": "uploaded" }
```

### `GET /workspaces/{workspace_id}/imports/{import_batch_id}`
Returns processing status, row counts, validation errors, and duplicate warnings.

## Accounts and events

### `GET /workspaces/{workspace_id}/accounts`
Query params: `stage`, `value_tier`, `next_touch_before`, `search`, `limit`, `cursor`.

### `GET /workspaces/{workspace_id}/accounts/{account_id}`
Returns account profile, contacts, order history, tasks, and message drafts.

### `POST /workspaces/{workspace_id}/events`
Creates a manual catering inquiry/order/event.

Request:
```json
{
  "organization_name": "Northside Clinic",
  "contact": { "name": "Pat", "email": "pat@clinic.example", "phone": "+15555555555" },
  "event_type": "healthcare_rep",
  "event_date": "2026-07-10",
  "headcount": 28,
  "estimated_value": 520,
  "status": "quote_sent",
  "dietary_notes": "vegetarian options requested"
}
```

## Follow-up queue

### `GET /workspaces/{workspace_id}/followups`
Query params: `status`, `due_before`, `priority`, `task_type`, `assigned_to`, `limit`, `cursor`.

### `PATCH /workspaces/{workspace_id}/followups/{task_id}`
Request:
```json
{
  "status": "completed",
  "staff_note": "Called and confirmed next office lunch date.",
  "snooze_until": null
}
```

### `POST /workspaces/{workspace_id}/followups/{task_id}/drafts/regenerate`
Request:
```json
{
  "channel": "email",
  "instructions": "Make it shorter and mention holiday trays without quoting prices."
}
```

## Message drafts

### `PATCH /workspaces/{workspace_id}/message-drafts/{draft_id}`
Updates subject/body/status after staff review.

Request:
```json
{
  "subject": "Catering for your next team lunch?",
  "body": "Hi Pat...",
  "status": "approved"
}
```

### `POST /workspaces/{workspace_id}/exports/followups`
Exports selected approved drafts/tasks to CSV or Markdown.

Request:
```json
{
  "task_ids": ["task_1", "task_2"],
  "format": "csv",
  "exclude_suppressed_contacts": true
}
```

## Revenue attribution

### `POST /workspaces/{workspace_id}/revenue-attributions`
Request:
```json
{
  "follow_up_task_id": "task_123",
  "amount": 685,
  "attribution_type": "recovered",
  "note": "Customer reordered after approved follow-up email."
}
```

## Admin endpoints

### `GET /admin/imports`
Internal-only import queue.

### `POST /admin/imports/{import_batch_id}/reprocess`
Reprocesses a failed import after mapping correction.

### `GET /admin/workspaces/{workspace_id}/audit-events`
Returns audit log for support/security review.

## Error format

```json
{
  "error": {
    "code": "SUPPRESSED_CONTACT",
    "message": "This contact is opted out or marked do-not-contact.",
    "request_id": "req_123"
  }
}
```
