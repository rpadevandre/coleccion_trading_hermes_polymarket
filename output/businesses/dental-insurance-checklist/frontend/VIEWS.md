# Frontend Views — Dental Insurance Checklist Assistant

Lightweight page skeleton notes only; no full app build in this repo.

## 1. Marketing landing page

Purpose: convert dental offices into checklist audit/pilot leads.

Sections:

- Hero: “Make dental insurance verification less painful before the patient arrives.”
- Pain bullets: denied/delayed claims, missing documentation, same-day surprises, staff burnout.
- ROI calculator: patients/week, minutes/verification, hourly cost, rework percentage.
- Before/after example: messy payer note -> structured benefit summary.
- Offer: 25-case verification checklist audit.
- CTA: request audit / book call.
- Compliance note: mock/sanitized examples only during validation.

## 2. Verification queue

Practice-facing working list:

- Patient mock ID.
- Appointment date.
- Procedure/appointment type.
- Payer.
- Status: not started, in progress, missing info, ready for review, approved.
- Exception flags.
- Owner.

## 3. Verification task detail

Panels:

- Appointment context.
- Procedure-specific checklist.
- Staff-entered payer notes.
- Extracted benefit fields.
- Missing/uncertain fields.
- PMS-ready note draft.
- Patient missing-info draft.
- Human approval actions.

## 4. Template library

Templates for:

- New patient exam.
- Hygiene recall.
- Crown.
- SRP/perio.
- Implant consult.
- Ortho consult.
- Emergency visit.

Each template includes required fields, optional fields, red flags, and suggested language.

## 5. Audit/demo report

For validation:

```text
Case #7 — Crown consult
Problem: missing frequency limitation + deductible status
Checklist output: ask payer X, capture waiting period, verify crown replacement clause
PMS note draft: ...
Time saved estimate: 8 minutes
```

## 6. Patient missing-info page (future)

Human-approved only:

- Upload insurance card.
- Confirm subscriber name/DOB.
- Confirm employer/group if needed.
- Neutral disclaimer: benefit review is not a guarantee of payer payment.
