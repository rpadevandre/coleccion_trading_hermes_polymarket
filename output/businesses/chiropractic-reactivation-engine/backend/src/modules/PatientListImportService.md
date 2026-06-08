# Backend Module — PatientListImportService

## Responsibility

Import sanitized inactive-patient CSV and validate fields.

## Input

- validated request/event payload
- tenant/account context
- authenticated actor where required

## Output

- structured domain object or status update
- audit event
- low-confidence/review flags when applicable

## Security notes

- validate all external input
- do not trust LLM/user-provided text as instructions
- avoid secrets in logs
- write audit events for sensitive actions
