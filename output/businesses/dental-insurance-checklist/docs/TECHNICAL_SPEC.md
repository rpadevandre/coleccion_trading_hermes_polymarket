# Technical Spec — Dental Insurance Checklist Assistant

Internal planning artifact only. No deployment, no production credentials, no real patient data, and no claims submission from this repo. The product is an AI-assisted checklist and documentation workflow for dental insurance verification; it is not a payer integration platform in v0.

## Product thesis

Dental front desks spend high-value staff time verifying eligibility, benefits, frequencies, waiting periods, deductibles, maximums, and documentation requirements. Mistakes create denied/delayed claims, surprise patient balances, and treatment-plan friction. The MVP helps teams run a repeatable pre-visit checklist and produce a clean benefit summary for human review.

## Narrow MVP buyer

- 1-5 location dental practice or small DSO.
- Office manager, practice owner, treatment coordinator, or insurance coordinator.
- English-speaking markets first: US practices are the primary validation target because dental insurance complexity is high.
- Existing systems may include Dentrix, Eaglesoft, Open Dental, Curve, spreadsheet trackers, payer portals, phone calls, and clearinghouses.

## Non-goals for v0

- No automated claim submission.
- No medical/dental advice.
- No guarantee of payer coverage or reimbursement.
- No production EDI integration until compliance, BAAs, and workflow validation are handled.
- No storage of real PHI in this internal repo.

## Frontend surface

### Buyer landing page

- Headline: “Make dental insurance verification less painful before the patient arrives.”
- Pain: denied claims, same-day surprises, incomplete notes, repeated payer checks.
- CTA: “Get a 25-patient verification checklist audit.”
- ROI calculator: verification minutes/patient, new patients/month, re-verifications/month, coordinator hourly cost, denied/delayed claim estimate.

### Practice user workflow

- Patient verification task list.
- Checklist by appointment type: new patient exam, hygiene, crown, implant consult, perio, ortho, emergency.
- Payer call/portal note template.
- Benefit summary draft.
- PMS-ready note copy block.
- Exception flags: missing subscriber info, inactive coverage, waiting period, frequency limitation, coordination of benefits, prior authorization/pre-determination needed.

### Patient-facing optional page

Future only, and human-approved:

- Request missing insurance card/photo.
- Ask for subscriber DOB/employer if missing.
- Display neutral language: “Your dental team is reviewing benefits; this is not a guarantee of payment.”

## Backend motor

### Pipeline

1. **Create verification task** from appointment and patient mock record.
2. **Select checklist template** based on procedure/appointment type.
3. **Capture verification evidence** from staff-entered payer portal/phone notes.
4. **AI-assisted extraction** into structured benefit fields.
5. **Rule checks** for missing fields, frequency limits, waiting period flags, deductible/max status, documentation requirements.
6. **Generate human-reviewed summary** for treatment coordinator/PMS note.
7. **Audit log** every edit, output, and approval.

### Suggested modules

- `task_service`: creates and updates verification tasks.
- `checklist_template_service`: procedure-specific required fields.
- `benefit_extraction_service`: turns staff notes into structured draft fields.
- `coverage_rules_service`: deterministic completeness and exception flags.
- `summary_drafter`: plain-language internal benefit summary.
- `patient_message_drafter`: optional missing-info request, never guarantee coverage.
- `audit_service`: immutable action log.
- `metrics_service`: verification time, completion rate, exception rate, denial feedback loop.

## Admin panel

- Verification queue: due date, appointment date, payer, status, exception flags.
- Task detail: patient mock ID, appointment type, checklist, extracted fields, source notes, approval state.
- Template manager: required fields per procedure and payer-type.
- Exception dashboard: inactive coverage, missing subscriber info, pre-auth likely, waiting period, frequency limitation.
- Metrics: completion before appointment, average verification time, same-day surprise count, claim issue feedback.
- Compliance settings: PHI handling notes, retention policy, user roles, human approval requirements.

## AI behavior contract

- Never state that insurance “will pay.” Use “benefits indicate,” “subject to payer processing,” and “not a guarantee.”
- Never invent missing payer information.
- Mark uncertainty explicitly.
- Extract from provided notes only.
- Ask for human review before patient-facing or PMS-ready output.
- Avoid clinical advice; stay within administrative benefits/checklist workflow.

## Security / compliance planning

Future production must treat patient identity, appointment details, insurance details, and payer notes as PHI-adjacent or PHI depending on implementation. Production planning should include HIPAA-oriented controls, BAAs with vendors, least-privilege access, audit trails, encryption, retention limits, and safe model/provider selection. This internal repo uses mock data only.

## Integrations roadmap

- Phase 1: manual checklist + copy/paste payer notes + CSV export.
- Phase 2: PMS-ready notes and task imports from spreadsheet.
- Phase 3: clearinghouse/payer portal workflow helpers where allowed.
- Phase 4: deeper PMS integrations only after paid validation and compliance design.

## Validation-ready success metrics

- Reduce manual verification documentation time by 30-50% on sample cases.
- Increase “complete before appointment” rate for selected appointments.
- Reduce missing-information exceptions at check-in.
- Get at least 3 offices to pay for a concierge audit or pilot before full build.

## Source notes

See `docs/SOURCES.md` for URLs used to frame dental insurance administrative burden, claim-denial concerns, and documentation/completeness risks.
