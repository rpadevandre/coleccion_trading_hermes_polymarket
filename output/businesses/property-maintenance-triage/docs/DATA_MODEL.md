# Data Model — Property Maintenance Triage

Internal markdown data sketch. Keep demo data synthetic.

## Entities

### Portfolio

- `id`
- `company_name`
- `door_count_band`: `20_50`, `51_100`, `101_300`, `300_plus`
- `market`: English-speaking rental markets first.
- `office_hours`
- `emergency_policy`
- `default_vendor_instructions`
- `created_at`, `updated_at`

### Property

- `id`
- `portfolio_id`
- `name`
- `address_stub` (city/state only in demo)
- `property_type`: `single_family`, `duplex`, `small_multifamily`, `hoa`, `commercial_light`
- `units_count`
- `preferred_vendor_rules`

### Unit

- `id`
- `property_id`
- `unit_label`
- `occupancy_status`
- `synthetic_tenant_ref`

### MaintenanceRequest

- `id`
- `portfolio_id`
- `property_id`
- `unit_id`
- `source`: `tenant_form`, `sms_demo`, `email_demo`, `manager_entry`
- `raw_message`
- `category`: `plumbing`, `hvac`, `electrical`, `appliance`, `lockout`, `pest`, `general`, `unknown`
- `urgency`: `emergency`, `urgent`, `routine`, `low`, `needs_review`
- `status`: `new`, `needs_info`, `triaged`, `approved`, `dispatched`, `scheduled`, `resolved`, `closed`
- `sla_due_at`
- `risk_flags`: array of safety/liability flags.

### Attachment

- `id`
- `request_id`
- `type`: `photo`, `video`, `document`
- `storage_ref_demo`
- `caption`
- `safe_for_vendor`

### TriageResult

- `id`
- `request_id`
- `model_version`
- `category_prediction`
- `urgency_prediction`
- `confidence`
- `missing_info_questions`
- `tenant_reply_draft`
- `vendor_route_suggestion`
- `human_override_reason`

### Vendor

- `id`
- `portfolio_id`
- `trade`
- `service_area`
- `after_hours_allowed`
- `insurance_status_manual`
- `preferred_contact_method`

### WorkOrder

- `id`
- `request_id`
- `vendor_id`
- `title`
- `scope_summary`
- `tenant_access_notes`
- `dispatch_status`
- `scheduled_window`
- `estimated_cost_band`

### AuditEvent

- `id`
- `portfolio_id`
- `actor_type`: `tenant_demo`, `manager`, `admin`, `ai_agent`, `system`
- `entity_type`, `entity_id`
- `event_name`
- `before_hash`, `after_hash`
- `created_at`

## Relationships

- One `Portfolio` has many `Properties`, `Vendors`, `MaintenanceRequests` and `RoutingRules`.
- One `MaintenanceRequest` has many `Messages`, `Attachments`, `TriageResults` and optionally one active `WorkOrder`.
- Every triage decision and human override generates an `AuditEvent`.

## MVP Storage Notes

- Postgres for workflow data.
- Object storage only for demo photo metadata; avoid real tenant photos in prototype.
- Queue worker for triage jobs and vendor-message drafting.
