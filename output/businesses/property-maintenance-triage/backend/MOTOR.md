# Backend Motor — Property Maintenance Triage

The backend motor turns unstructured maintenance reports into structured, auditable work orders. It should be deterministic where safety matters and AI-assisted where language cleanup/classification improves speed.

## Core event flow

```text
request_submitted
  -> validate_required_fields
  -> run_emergency_rules
  -> normalize_media_metadata
  -> classify_issue
  -> detect_missing_information
  -> draft_tenant_followup_or_work_order
  -> queue_for_human_review
  -> admin_approved
  -> vendor_or_tenant_message_ready
```

## Inputs

- Tenant form submissions.
- Manual admin-entered requests.
- Future: SMS/email webhook parser.
- Future: PMS work-order import/export.

## Outputs

- Structured maintenance request.
- Urgency classification: emergency, urgent, routine, incomplete, duplicate.
- Category/trade: plumbing, HVAC, electrical, appliance, lock/security, pest, general.
- Missing-info checklist.
- Tenant response draft.
- Vendor-ready work-order summary.
- Immutable audit events.

## Deterministic rules first

Safety categories must not rely on free-form AI alone:

- Gas smell.
- Active fire/smoke.
- Flooding or active major leak.
- Electrical sparking/burning smell.
- Broken exterior lock/security breach.
- No heat/cooling when legally/regionally time-sensitive.

These create `safety_flag=true`, force human/admin attention, and can display tenant emergency guidance.

## AI triage JSON contract

Expected structured output:

```json
{
  "category": "plumbing",
  "urgency": "urgent",
  "confidence": 0.84,
  "summary_for_manager": "Tenant reports active leak under kitchen sink...",
  "missing_information": ["photo of leak source", "permission to enter"],
  "recommended_trade": "plumber",
  "tenant_reply_draft": "Thanks — please upload a photo...",
  "vendor_work_order_draft": "Kitchen sink leak; tenant says...",
  "risk_flags": ["possible water damage"]
}
```

## Human approval gates

- Sending vendor dispatch message.
- Sending tenant message beyond receipt confirmation.
- Marking request duplicate.
- Closing request.
- Changing emergency/urgent classification downward.

## Metrics

- Request count by category.
- Average time to first admin review.
- Average time to vendor-ready work order.
- Clarification rate.
- Emergency flag count.
- AI classification overridden by admin.

## Testing with mock data

Seed examples should include:

- Vague routine issue: “the thing under the sink is wet.”
- True emergency: “water pouring through ceiling.”
- False alarm: “AC is loud but working.”
- Duplicate request.
- Missing unit/access info.
- Spanish-language tenant message for future bilingual stress test.
