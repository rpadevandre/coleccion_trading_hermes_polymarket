# Backend Services

- `PatientListImportService` — Import sanitized inactive-patient CSV and validate fields.
- `ReactivationSegmenter` — Segment by recency, visit type, last status and consent/eligibility.
- `MessageDraftService` — Draft gentle rebooking/nurture messages for staff approval.
- `OptOutSuppressionService` — Track opt-outs and suppress future contact.
- `RecoveredAppointmentTracker` — Track replies, booked appointments and recovery metrics.
