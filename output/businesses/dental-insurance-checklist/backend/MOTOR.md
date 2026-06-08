# Backend Motor — Dental Insurance Checklist Assistant

The backend motor organizes insurance verification tasks, extracts structured fields from staff-provided notes, flags missing information, and drafts reviewable summaries. It does not submit claims or guarantee coverage.

## Core event flow

```text
verification_task_created
  -> choose_procedure_template
  -> collect_staff_payer_notes
  -> extract_benefit_fields
  -> run_completeness_rules
  -> flag_exceptions
  -> draft_pms_note_and_patient_request
  -> queue_for_human_review
  -> approved_or_returned_for_more_info
```

## Inputs

- Mock patient/appointment data.
- Staff-entered payer portal notes.
- Staff-entered phone call notes.
- Procedure/checklist type.
- Future: spreadsheet imports or PMS task imports.

## Outputs

- Structured verification task.
- Benefit field draft.
- Missing-field list.
- Exception flags.
- PMS-ready note draft.
- Patient missing-info message draft.
- Audit trail.

## Field groups

- Subscriber: name, DOB, relationship, group/employer.
- Eligibility: active/inactive, effective date, termination date if known.
- Plan basics: plan type, deductible, annual max, used max, remaining max.
- Procedure benefits: coverage percent, frequency limits, waiting periods, exclusions.
- Administrative: prior authorization/pre-determination indicator, documentation requirements, payer reference number, staff initials/date.

## AI extraction JSON contract

```json
{
  "eligibility_status": "active",
  "confidence": 0.78,
  "deductible_individual": "$50",
  "annual_max_remaining": "$920",
  "procedure": "crown",
  "coverage_percent": "50%",
  "frequency_limit": "once every 5 years",
  "waiting_period_flag": false,
  "missing_fields": ["replacement clause", "payer reference number"],
  "uncertain_fields": ["annual max used"],
  "pms_note_draft": "Verified benefits for crown...",
  "patient_message_draft": "Please upload the back of your insurance card..."
}
```

## Deterministic guardrails

- If source note does not contain a field, mark it missing; never invent.
- If active/inactive is unclear, status is `uncertain`.
- Patient-facing copy must include “not a guarantee of payment” language.
- Any output used in PMS or sent externally requires human approval.
- Real PHI is prohibited in internal validation materials.

## Metrics

- Verification tasks completed before appointment.
- Average time in queue.
- Missing fields per task.
- Exception rate by procedure.
- Human override rate of AI-extracted fields.
- Paid audit conversion and pilot conversion.

## Mock test cases

- New patient with missing subscriber DOB.
- Crown with replacement clause unknown.
- SRP with frequency/periodontal documentation requirements.
- Inactive coverage discovered before appointment.
- Coordination of benefits uncertainty.
- Emergency patient with incomplete insurance card.
