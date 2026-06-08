# Validation Plan — Dental Insurance Checklist Assistant

## Validation objective

Prove that dental offices will pay for a focused pre-visit insurance verification checklist that saves staff time, reduces missing documentation, and prevents avoidable same-day treatment/payment surprises.

## First ICP

- US dental practices with 1-5 locations.
- 1+ person handling benefits verification weekly.
- Mix of PPO insurance patients and procedures that require detailed benefit checks.
- Existing workflow involves payer portals, phone calls, PMS notes, spreadsheets, or sticky-note processes.
- Buyer is practice owner, office manager, or small DSO ops lead.

## Discovery questions

1. How many patients are verified per week?
2. How long does each verification take for new patients vs existing patients?
3. Which procedures cause the most insurance surprises?
4. How often are claims delayed/denied because of missing documentation, eligibility, frequency, or coding/benefit issues?
5. Where do verification notes live today?
6. What happens when insurance information is incomplete on appointment day?
7. Who reviews benefit summaries before treatment presentation?
8. What would a reliable checklist be worth if it saved coordinator time and reduced surprises?

## Smoke test offer

**Offer:** “We will review 25 sanitized verification cases and return a standardized checklist pack: missing fields, procedure-specific verification prompts, PMS-ready note templates, and patient missing-info message drafts.”

- Paid audit target: $249-$750.
- Pilot target: $399-$999/month depending on office size and verification volume.
- Success threshold: 3 paid audits or 2 paid pilots from 30 qualified offices.

## Concierge MVP

1. Office provides sanitized examples or mock/recreated verification notes with patient identifiers removed.
2. Internal operator maps each case to the checklist template.
3. AI-assisted extraction drafts structured benefit fields from notes.
4. Human reviews and produces a benefit-summary template.
5. Office manager rates usefulness, time saved, and willingness to pay.

## Money-focused ROI model

Inputs:

- Verifications/week.
- Average minutes per verification.
- Coordinator hourly cost.
- Percent needing rework/missing info.
- Average delayed/denied claim admin cost estimate.

Formula:

`monthly_time_savings = weekly_verifications * minutes_saved / 60 * hourly_cost * 4.33`

Add qualitative upside:

- Fewer check-in surprises.
- Cleaner treatment coordinator handoff.
- Better documentation when payer requests additional info.

## Landing-page experiment

Headline: “Make dental insurance verification less painful before the patient arrives.”

CTA: “Get a 25-case verification checklist audit.”

Track:

- Qualified office visitor to CTA click.
- CTA click to booked call.
- Booked call to paid audit.
- Paid audit to pilot.

## Procedure templates to test first

- New patient exam / hygiene.
- Crown.
- Scaling and root planing.
- Implant consult.
- Ortho consult.
- Emergency visit.

## Red flags / invalidation

- Offices already have a highly automated clearinghouse/PMS workflow with little manual burden.
- Buyer sees verification as low-value admin and refuses even a paid audit.
- Compliance/security requirements exceed the budget and timeline for a small MVP.
- Payer variability prevents repeatable checklist design.

## Evidence to collect

- Time per verification before/after checklist.
- Number of missing fields caught before appointment.
- Staff satisfaction with PMS-ready note format.
- Denial/delay categories mentioned in interviews.
- Exact words buyers use to describe the pain.

## Next action checklist

- Build mock 25-case audit packet with fake patient data.
- Interview 20 office managers/insurance coordinators.
- Run 5 paid or discounted audits.
- Do not build payer integrations until concierge workflow converts.
