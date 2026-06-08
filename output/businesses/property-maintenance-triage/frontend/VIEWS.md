# Frontend Views — Property Maintenance Triage

Lightweight UI/page skeleton notes only. No full app build in this repo.

## 1. Marketing landing page

Purpose: convert property managers into audit/pilot leads.

Sections:

- Hero: “Turn vague tenant maintenance messages into vendor-ready work orders.”
- Pain bullets: after-hours texts, missing photos, wrong vendor dispatch, no audit trail.
- ROI calculator: units, requests/month, minutes/request, hourly cost.
- Demo cards: plumbing leak, HVAC not cooling, appliance failure, lock/security issue.
- Offer: 20-request triage audit.
- CTA: book call / request audit.

Pseudo-layout:

```text
Hero
  headline
  subhead
  CTA: Get a 20-request triage audit
  secondary: View sample triage report
ROI Calculator
Sample Inbox Preview
How It Works: ingest -> triage -> approve -> route
Security/Privacy Note
FAQ
```

## 2. Tenant maintenance intake

Mobile-first, minimal friction.

Fields:

- Property/unit selector or manual address token.
- Tenant name/contact.
- Issue category or “not sure.”
- Description.
- Photo/video upload prompts.
- Permission to enter.
- Pets/safety/access notes.
- Emergency acknowledgment for gas/fire/flooding/electrical hazards.

Behavior:

- If emergency keywords are selected, show immediate safety instructions and flag admin.
- If category-specific evidence is missing, request it inline before submit.
- Tenant sees status page link after submission.

## 3. Request status page

Tenant-facing status only:

- Received.
- Clarification needed.
- Under manager review.
- Vendor contacted.
- Scheduled.
- Completed.

Never show internal AI confidence, landlord notes, vendor pricing, or tenant risk labels.

## 4. Manager sample report page

Used during validation before full product build.

Cards:

- “Before”: messy tenant message.
- “After”: category, urgency, vendor type, missing info, tenant reply, work-order summary.
- Time saved estimate.
- Button: approve/edit sample.

## 5. Accessibility / language

- English-first for buyer-facing pages.
- Spanish public-content available for future bilingual marketing.
- Tenant intake should be designed so text can be translated later without changing workflow logic.
