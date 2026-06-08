# Technical Spec — Property Maintenance Triage

Internal planning artifact only. No deployment, no production credentials, and no real tenant/customer data. This business is designed for English-speaking property managers first, with Spanish public-content and future bilingual tenant intake as an expansion path.

## Product thesis

Small property managers lose time and margin when tenant maintenance messages arrive as vague texts, photos, voicemails, and email threads. The MVP is not a full property-management platform; it is a triage layer that converts incomplete tenant reports into reviewable work orders, assigns urgency, requests missing evidence, and prepares vendor/tenant communication for human approval.

## Narrow MVP buyer

- Independent property manager or landlord/operator with 20-300 units.
- Has at least one part-time coordinator or owner-operator personally handling maintenance messages.
- Uses AppFolio, Buildium, Doorloop, Google Workspace, email, SMS, or spreadsheets, but still receives many off-system messages.
- Monetizable pain: after-hours disruption, repeated clarifying messages, slow emergency escalation, vendor dispatch errors, and poor documentation during deposit/dispute situations.

## Non-goals for v0

- No automated emergency dispatch without human approval.
- No rent collection, accounting, lease management, or full PMS replacement.
- No vendor marketplace.
- No tenant screening.
- No storage of production tenant data in this repo.

## Frontend surface

### Tenant intake

- Mobile-first maintenance request form.
- Required fields: property/unit selector, issue category, free-text description, urgency claim, permission to enter, pets present, preferred contact method.
- Guided photo prompts by category: plumbing leak, HVAC, appliance, electrical, lock/security, pest, general.
- Safety branch: if the request indicates active fire, gas smell, flooding, sparking, break-in, or medical danger, show emergency instructions and flag admin.

### Tenant status page

- Shows request received, clarification needed, under manager review, vendor assigned, scheduled, completed.
- Displays only safe tenant-facing data; hides internal notes, vendor pricing, and risk scores.

### Manager demo / validation flow

- ROI calculator: units managed, maintenance requests/month, average minutes per request, coordinator hourly cost, after-hours volume.
- Sample inbox using mock tenants and mock units.
- CTA: “Send 20 messy maintenance messages and we will return a triage report.”

## Backend motor

### Pipeline

1. **Ingest**: receive request from form, SMS/email parser placeholder, or manual admin entry.
2. **Normalize**: map input to canonical request schema, clean phone/email, attach media metadata.
3. **Safety screen**: deterministic keyword/rule pass for emergencies before any generative step.
4. **AI classification**: category, urgency, likely trade, missing information, tenant-friendly summary.
5. **Clarification planner**: select 1-3 follow-up questions only when needed; avoid long back-and-forth.
6. **Work-order composer**: create manager-facing vendor-ready summary with evidence checklist.
7. **Human review**: admin approves, edits, rejects, or marks duplicate.
8. **Audit log**: every status change, AI output, and message draft is immutable.

### Suggested services / modules

- `intake_service`: validates inbound request, creates request record.
- `triage_rules`: emergency and compliance guardrails.
- `ai_triage_service`: structured model call returning JSON only.
- `media_service`: stores mock metadata; future signed upload URLs.
- `vendor_router`: maps category + property rules to vendor candidates.
- `message_drafter`: tenant/vendor response drafts.
- `audit_service`: append-only event log.
- `metrics_service`: SLA, response time, first-touch completeness, and saved-hours estimates.

## Admin panel

- Inbox grouped by emergency, urgent, routine, incomplete, duplicate.
- Request detail: tenant input, media, AI summary, risk flags, missing info, proposed vendor trade.
- Clarification queue: one-click approve/edit/send tenant follow-up.
- Vendor routing: preferred vendors per property, category, hours, insurance status.
- Property/unit directory: lightweight mock records for validation demos.
- SLA dashboard: time-to-first-response, time-to-work-order, after-hours requests, prevented duplicates.
- Settings: category taxonomy, emergency rules, message templates, disclosure text.

## AI behavior contract

- Return structured JSON with confidence values and reasons.
- Never tell a tenant that a repair is guaranteed, covered, or scheduled unless admin status says so.
- Escalate safety issues and uncertainty to human review.
- Preserve original tenant wording in audit notes; do not overwrite evidence.
- Draft concise, plain-language tenant messages.

## Data retention / privacy planning

- V0 validation uses mock data or prospect-supplied sanitized examples only.
- Future production: tenant PII, photos, phone numbers, and unit addresses are sensitive operational data.
- Provide configurable retention windows for closed requests and media.
- Role-based access: owner/admin/coordinator/vendor-readonly.
- Vendor view should only expose job-relevant information, not tenant financial/lease data.

## Integrations roadmap

- Phase 1: form intake + manual export CSV/PDF.
- Phase 2: email forwarding parser, SMS provider webhook, Slack/Teams notifications.
- Phase 3: PMS work-order push for AppFolio/Buildium/Doorloop where API access exists; otherwise email-to-work-order format.
- Phase 4: vendor scheduling links and cost/quote comparison.

## Validation-ready success metrics

- Reduce average coordinator triage time by 50%+ on sampled requests.
- Convert 80%+ of vague requests into manager-usable work orders without more than one follow-up.
- Detect all obvious emergency/safety cases in a seeded test set.
- Get 3+ property managers to pay or commit to a paid pilot before full build.

## Source notes

See `docs/SOURCES.md` for URLs used to frame market pain, including property-management time burden and maintenance prioritization references.
