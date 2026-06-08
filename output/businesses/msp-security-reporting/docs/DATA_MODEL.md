# Data Model

## Core entities

- Account / Tenant
- User
- Role
- InboundItem
- Classification
- AIOutput
- ReviewDecision
- WorkflowStatus
- AuditEvent
- MetricSnapshot
- IntegrationCredentialReference — reference only; no raw secrets in app logs/docs.

## Notes

Keep the MVP relational and auditable. Prefer simple Postgres/SQLite-compatible models first, then integrations later.
