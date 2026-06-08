# Technical Spec — HVAC Missed-Call Recovery

## Canonical MVP scope

Build an internal-ready missed-call recovery motor for small HVAC contractors that turns unanswered calls into a structured callback/SMS workflow, emergency triage queue, and recovered-revenue dashboard. No deployment, no secrets, and no real customer data in this repo.

## Buyer workflow being automated

1. A prospect calls the HVAC shop after hours, during lunch, or while dispatch is overloaded.
2. Phone provider/webhook records a missed call or voicemail event.
3. The system immediately sends a compliant SMS acknowledgement if the business has permission to text.
4. The caller is asked for the minimum details needed: issue type, property zip/postcode, urgency, heating/cooling status, name, callback number.
5. AI classifies emergency vs routine, summarizes the job, and suggests next action.
6. Human dispatcher or on-call tech approves callback, booking, or deferral.
7. Dashboard tracks callback SLA, booked jobs, estimated ticket value, and recovered revenue.

## Frontend/client-facing surface

- Public landing page with ROI calculator based on missed calls/month, booking rate, and average service ticket.
- “Missed Call Audit” intake form for prospects to request a free review.
- Demo simulator showing a missed AC emergency moving from call event to SMS to dispatcher queue.
- Lightweight customer portal for pilot clients to view missed calls, callbacks, bookings, and settings.

## Backend services

- `call_event_ingestor`: normalizes missed-call, voicemail, form, and SMS events.
- `contact_resolver`: matches phone number to existing lead/customer or creates a new lead.
- `triage_classifier`: AI-assisted urgency classification with deterministic rules for safety words like no heat, no cooling, gas smell, elderly resident, infant, medical risk.
- `message_composer`: drafts SMS/callback scripts from approved templates.
- `routing_engine`: chooses owner, dispatcher, or on-call tech based on hours, territory, and urgency.
- `roi_meter`: estimates recovered value using client-configured average ticket and confirmed booking outcomes.
- `audit_logger`: immutable event history for every AI suggestion, human override, outbound message, and status change.

## Integrations to design for later

- Phone/SMS: Twilio, OpenPhone, CallRail, Aircall, RingCentral.
- Calendar/booking: Google Calendar, Housecall Pro, ServiceTitan, Jobber as future adapters.
- CRM/export: CSV, webhook, Zapier/Make, HubSpot.
- Notifications: email, Slack, SMS escalation to on-call technician.

## Data requirements

- Do not store call recordings in the MVP unless explicitly needed; prefer metadata and transcripts from provider if available.
- Store opt-in/consent fields before automated SMS.
- Use mock phone numbers and synthetic names in repo fixtures.
- Retain message/event logs for pilot reporting; define deletion/export flow before production.

## AI boundaries

- AI may classify, summarize, and draft.
- AI may not diagnose HVAC equipment, quote exact repair prices, make safety guarantees, or confirm appointments without human/business-rule approval.
- Emergency language must escalate to a human/on-call route rather than a generic chatbot loop.

## MVP acceptance criteria

- Ingest synthetic missed-call event and create a lead within 2 seconds in local tests.
- Generate a triage summary with urgency, issue category, location, and recommended route.
- Show dispatcher queue sorted by emergency risk and time since missed call.
- Track whether callback happened within 5/15/30 minutes.
- Calculate pilot ROI from confirmed bookings, not from raw AI assumptions.

## Original technical notes

The older `TECH_SPEC.md` file is preserved for compatibility. This file is the canonical checklist target.
