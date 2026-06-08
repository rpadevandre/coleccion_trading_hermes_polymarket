# Technical Spec — Chiropractic Patient Reactivation Engine

## Canonical MVP scope

Build an internal-ready patient reactivation workflow for chiropractic clinics that helps staff identify inactive patients, draft compliant outreach, approve messages, track rebooked appointments, and report recovered revenue. No deployment, no secrets, no real patient/customer data in this repo.

## Buyer workflow being automated

1. Clinic exports or manually enters a synthetic inactive-patient list for pilot modeling.
2. System segments records by last visit date, care-plan status, appointment type, insurance/cash-pay indicator if available, and communication eligibility.
3. AI drafts low-pressure recall messages using approved templates and clinic tone.
4. Staff reviews/approves messages before any outbound send.
5. Replies are triaged into booked, interested, not now, opt-out, wrong number, or needs staff call.
6. Booked appointment and attended appointment outcomes are tracked.
7. Dashboard reports campaign ROI using collected/estimated visit revenue supplied by the clinic.

## Frontend/client-facing surface

- Landing page centered on “recover existing patient revenue before buying more ads.”
- ROI calculator using inactive patient count, reachable rate, booking rate, show rate, and average visit value.
- Demo flow: upload mock CSV → segment → approve message → track appointment outcome.
- Clinic portal views for campaign setup, message approvals, patient status, and revenue report.

## Backend services

- `patient_importer`: validates CSV/manual entries and blocks PHI-heavy fields not needed for MVP.
- `eligibility_filter`: suppresses opt-outs, recent contacts, minors without guardian workflow, and records missing consent status.
- `segmentation_engine`: groups patients by inactivity window, likely intent, and recommended campaign.
- `message_drafter`: creates non-diagnostic, non-coercive reactivation copy from approved templates.
- `approval_queue`: requires human review before outbound communication.
- `reply_classifier`: labels inbound replies and escalates clinical/billing questions to staff.
- `appointment_tracker`: maps booked/attended/no-show outcomes to campaign and patient segment.
- `roi_reporter`: calculates recovered revenue from booked/attended outcomes, not from raw send volume.
- `audit_logger`: records imports, model prompts/outputs, staff approvals, outbound messages, opt-outs, and status changes.

## Compliance and privacy assumptions

- US pilots must be designed with HIPAA-aware workflows; the repo itself contains only synthetic data.
- Minimize PHI: avoid diagnoses and treatment notes in prompts/messages.
- Use clinic-approved templates and staff approval until legal/compliance review says otherwise.
- Provide opt-out handling and suppression lists from day one.
- Add Business Associate Agreement and production hosting controls before any real PHI touches the system.

## AI boundaries

- AI may segment, summarize, and draft reminder/reactivation language.
- AI may not provide medical advice, diagnose, change care plans, promise outcomes, discuss insurance coverage, or independently message patients.
- Clinical, billing, injury, emergency, or complaint replies must route to clinic staff.

## MVP acceptance criteria

- Import a mock inactive-patient CSV and produce eligible/suppressed counts.
- Generate segment-specific message drafts from approved templates.
- Require staff approval before marking a message as ready to send.
- Classify synthetic replies with confidence and escalation reason.
- Show recovered-revenue report based on booked and attended appointments.

## Original technical notes

The older `TECH_SPEC.md` file is preserved for compatibility. This file is the canonical checklist target.
