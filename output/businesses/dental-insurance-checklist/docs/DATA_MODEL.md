# Data Model — Dental Insurance Checklist Assistant

Internal markdown data sketch. Keep all examples synthetic.

## Entities

### Practice

- `id`
- `name`
- `market`: US, Canada, UK private dentistry where applicable.
- `office_hours`
- `verification_sop`
- `default_disclaimer`
- `payer_watchlist`
- `created_at`, `updated_at`

### User

- `id`
- `practice_id`
- `role`: `owner`, `office_manager`, `insurance_coordinator`, `front_desk`, `readonly_admin`
- `email_hash`
- `mfa_enabled`
- `last_login_at`

### Visit

- `id`
- `practice_id`
- `synthetic_patient_ref` for demo; real patient IDs prohibited until compliant build.
- `appointment_datetime`
- `appointment_type`
- `provider_ref`
- `status`: `new`, `needs_verification`, `waiting_on_patient`, `waiting_on_payer`, `verified`, `exception`, `closed`
- `financial_risk_score`: 1-5 based on high-ticket procedures, inactive plans and missing plan details.

### CoverageSnapshot

- `id`
- `visit_id`
- `payer_name`
- `plan_name`
- `subscriber_relationship`
- `eligibility_status`
- `annual_maximum`, `remaining_maximum`, `deductible`, `deductible_remaining`
- `frequency_limit_notes`
- `waiting_period_notes`
- `coordination_of_benefits_notes`
- `source_type`: `manual_call`, `portal`, `patient_upload`, `demo_seed`

### ChecklistItem

- `id`
- `visit_id`
- `category`: `eligibility`, `benefits`, `limitations`, `patient_followup`, `office_note`, `financial_consent`
- `label`
- `instructions`
- `status`: `open`, `complete`, `blocked`, `not_applicable`
- `evidence_ref`
- `updated_by_user_id`

### GeneratedNote

- `id`
- `visit_id`
- `note_type`: `pms_internal`, `patient_summary`, `payer_call_script`, `front_desk_task`
- `draft_text`
- `review_status`: `draft`, `approved`, `rejected`
- `model_version`

### AuditEvent

- `id`
- `practice_id`
- `actor_type`: `user`, `system`, `ai_agent`
- `actor_id`
- `entity_type`, `entity_id`
- `event_name`
- `before_hash`, `after_hash`
- `created_at`

## Relationships

- One `Practice` has many `Users`, `Visits`, `Templates` and `AuditEvents`.
- One `Visit` has one active `CoverageSnapshot`, many `ChecklistItems`, many `GeneratedNotes`.
- All writes create `AuditEvent` records.

## MVP Storage Notes

- Use Postgres for relational workflow state.
- Store documents/photos only in non-production demo object storage; no real insurance cards in MVP skeleton.
- Encrypt sensitive fields at rest once a compliant version is built.
