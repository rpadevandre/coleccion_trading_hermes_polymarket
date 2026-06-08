# Backend Motor — Restaurant Catering Follow-Up Copilot

## Purpose

Help independent restaurants and small multi-location groups turn catering inquiries, quotes, and one-time orders into repeat catering revenue through structured follow-up, reminders, segmentation, and human-approved messaging.

## Core pipeline

1. **Lead/order ingest**
   - Import from CSV, website form, POS export, catering platform export, email parser, or manual entry.
   - Normalize contact, company, order size, date, dietary notes, event type, source, and last interaction.
2. **Account/contact matching**
   - Merge duplicate contacts by email/phone/company domain.
   - Link multiple contacts to one organization when possible.
   - Flag uncertain matches for admin review.
3. **Segmentation**
   - Classify into: quote requested, first-time order, repeat account, lapsed account, seasonal buyer, high-value account, low-fit lead.
   - Score value based on order size, recency, frequency, event type, and company type.
4. **Follow-up plan generation**
   - Build next-step schedule:
     - quote follow-up in 2 hours / 24 hours,
     - post-event thank-you,
     - reorder reminder near predictable cadence,
     - seasonal/event campaign,
     - lapsed account reactivation.
   - Generate message drafts with menu/order context and clear CTA.
5. **Human approval**
   - Restaurant staff approve, edit, or pause messages.
   - System never sends sensitive/allergy-specific recommendations without explicit review.
6. **Send/export**
   - MVP can export drafts to copy/paste, CSV, or email tool import.
   - Later integrations may send via email/SMS provider, but no auto-send by default.
7. **Revenue tracking**
   - Attribute orders manually or through uploaded order exports.
   - Show recovered revenue, follow-up conversion, repeat order cadence, and pipeline value.

## Key services

- `CateringLeadImportService`: handles CSV/form/manual ingest and validation.
- `ContactDeduplicationService`: merges duplicate people and organizations.
- `AccountSegmentationService`: assigns stage, value tier, and reorder likelihood.
- `FollowUpScheduleService`: creates next-touch tasks and campaign windows.
- `MessageDraftService`: generates email/SMS/call-note drafts using brand/menu context.
- `ApprovalQueueService`: enforces human review before send/export.
- `RevenueAttributionService`: maps follow-up activity to orders and estimated recovered revenue.
- `SuppressionService`: manages unsubscribes, do-not-contact, and quiet hours.

## Follow-up logic examples

- **Quote requested, no order**: send helpful reminder with deadline and event-size confirmation.
- **First-time order completed**: thank-you, ask for feedback, offer recurring office lunch plan.
- **High-value corporate account**: schedule monthly check-in and holiday planning reminder.
- **Lapsed account**: reactivate with seasonal menu, minimum order reminder, and easy reorder CTA.
- **Event-specific buyer**: remind 30-45 days before the likely annual event date.

## Safety and constraints

- Respect opt-out status and local SMS/email rules.
- Do not infer allergies beyond stored notes.
- Do not promise availability, delivery radius, or pricing unless current menu/admin rules support it.
- Route complaints or refund language to staff, not AI auto-response.

## Pseudocode

```pseudo
on LeadOrOrderImported(record):
  contact = dedupe_contact(record)
  account = find_or_create_account(contact.company)
  stage = classify_catering_stage(record, account.history)
  score = calculate_revenue_priority(record, account.history)
  schedule = build_followup_schedule(stage, score, record.event_date)
  drafts = generate_staff_review_drafts(schedule, account, restaurant.brand_rules)
  create_approval_tasks(drafts)
  update_dashboard_pipeline(account, score, schedule.next_touch)
```
