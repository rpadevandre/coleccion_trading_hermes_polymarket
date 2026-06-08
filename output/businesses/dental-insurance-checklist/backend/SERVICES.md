# Backend Services

- `VerificationIntakeService` — Capture patient/procedure/plan metadata without storing unnecessary PHI.
- `ChecklistBuilder` — Generate procedure-specific verification checklist and missing fields.
- `PolicyLanguageSummarizer` — Summarize plan notes into staff-readable reminders with source references.
- `ComplianceGuard` — Flag PHI/compliance-sensitive handling and avoid payment guarantees.
- `VerificationAuditService` — Track checklist completion, edits and verification status.
