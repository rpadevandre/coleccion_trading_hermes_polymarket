# Data Model — Restaurant Catering Follow-Up Copilot

## Entities

### RestaurantWorkspace
- `id`
- `restaurant_name`
- `website`
- `location_count`
- `market`
- `plan_type`: audit, pilot, monthly, paused
- `timezone`
- `created_at`, `updated_at`

### Location
- `id`
- `workspace_id`
- `name`
- `address`
- `phone`
- `delivery_radius_notes`
- `catering_minimum_notes`

### StaffUser
- `id`
- `workspace_id`
- `location_ids[]`
- `name`
- `email`
- `role`: owner, manager, staff, viewer, internal_operator
- `mfa_enabled`
- `last_login_at`

### OrganizationAccount
- `id`
- `workspace_id`
- `name`
- `type`: office, school, healthcare, nonprofit, real_estate, church, unknown
- `domain`
- `value_tier`: high, medium, low, unknown
- `stage`: quote_pending, first_order, repeat, lapsed, disqualified
- `last_order_at`
- `next_likely_event_at`
- `notes`

### Contact
- `id`
- `workspace_id`
- `organization_account_id`
- `name`
- `email`
- `phone`
- `title`
- `preferred_channel`: email, phone, sms, unknown
- `opt_out_email`
- `opt_out_sms`
- `do_not_contact`

### CateringEvent
- `id`
- `workspace_id`
- `organization_account_id`
- `contact_id`
- `location_id`
- `event_type`: office_lunch, meeting, holiday, school, healthcare_rep, nonprofit, other
- `event_date`
- `headcount`
- `estimated_value`
- `actual_value`
- `status`: inquiry, quote_sent, ordered, completed, cancelled, lost
- `source`: web_form, phone, email, pos_export, platform_export, manual
- `dietary_notes`
- `created_at`, `updated_at`

### FollowUpTask
- `id`
- `workspace_id`
- `organization_account_id`
- `contact_id`
- `catering_event_id`
- `assigned_staff_user_id`
- `task_type`: quote_followup, post_event_thanks, reorder_reminder, seasonal_campaign, lapsed_reactivation, call_note
- `due_at`
- `priority`: urgent, high, medium, low
- `status`: pending, draft_ready, approved, completed, snoozed, cancelled
- `estimated_revenue_opportunity`

### MessageDraft
- `id`
- `follow_up_task_id`
- `channel`: email, sms, call_note
- `subject`
- `body`
- `personalization_tokens[]`
- `risk_flags[]`
- `status`: draft, needs_edits, approved, copied, sent_external, archived
- `created_by`: ai, human
- `created_at`, `updated_at`

### RevenueAttribution
- `id`
- `workspace_id`
- `follow_up_task_id`
- `catering_event_id`
- `amount`
- `attribution_type`: recovered, influenced, manual_note
- `entered_by_user_id`
- `created_at`

### ImportBatch
- `id`
- `workspace_id`
- `source_type`: csv, form, email_paste, manual, platform_export
- `status`: uploaded, mapped, processed, failed, quarantined
- `rows_total`
- `rows_imported`
- `rows_flagged`
- `error_report_key`

### AuditEvent
- `id`
- `workspace_id`
- `actor_user_id`
- `event_type`
- `entity_type`
- `entity_id`
- `reason_code`
- `created_at`

## Relationships

- Workspace has many Locations, StaffUsers, OrganizationAccounts, Contacts, ImportBatches.
- OrganizationAccount has many Contacts and CateringEvents.
- CateringEvent can have many FollowUpTasks.
- FollowUpTask can have many MessageDrafts.
- RevenueAttribution links follow-up tasks to resulting/influenced orders.
