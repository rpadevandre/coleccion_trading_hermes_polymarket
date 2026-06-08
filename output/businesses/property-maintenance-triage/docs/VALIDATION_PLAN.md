# Validation Plan — Property Maintenance Triage

## Validation objective

Prove that small property managers will pay for a focused maintenance triage layer before building a full application. The business must validate money saved, faster response, and better work-order quality with English-speaking property managers first.

## ICP for first 20 interviews

- 20-300 rental doors.
- Owner-operator, small property management firm, or maintenance coordinator.
- Receives maintenance through text, email, phone, or tenant portal and still has manual triage burden.
- Has recurring vendor dispatch or tenant clarification friction.
- US, Canada, UK, Australia, or other English-speaking property management market.

## Pain questions

1. How many maintenance requests do you receive per month?
2. What percent arrive with missing photos/details?
3. Who decides emergency vs urgent vs routine?
4. How many minutes does a coordinator spend before a request becomes vendor-ready?
5. What happens after hours?
6. Which mistakes cost the most: late emergency response, wrong vendor, duplicate trips, poor documentation, tenant dissatisfaction?
7. What system do you use today and where does it break?
8. Would you pay for a layer that creates clean work orders while preserving your existing PMS?

## Smoke test offer

**Offer:** “Send us 20 messy maintenance requests. In 48 hours we will return a triage report: urgency, trade, missing info, vendor-ready summary, and tenant response drafts. If it saves at least 2 hours, join a paid pilot.”

- Setup fee target: $199-$499 for the audit/report.
- Pilot target: $299-$799/month depending on units/request volume.
- Success threshold: 3 paid audits or 2 paid pilots from 30 qualified prospects.

## Landing-page test

Headline: “Turn vague tenant maintenance messages into vendor-ready work orders.”

Primary CTA: “Get a 20-request triage audit.”

Track:

- Qualified visitor to CTA click.
- CTA click to booked call.
- Booked call to paid audit.
- Paid audit to pilot conversion.

## Concierge MVP workflow

1. Prospect uploads sanitized sample requests or rewrites examples with names/addresses removed.
2. Internal operator runs requests through structured triage prompt and rules checklist.
3. Deliver spreadsheet/PDF: category, urgency, missing info, vendor type, tenant response, work-order summary.
4. Ask buyer to estimate time saved and willingness to pay.
5. Use feedback to tune categories, urgency language, and vendor routing.

## Money-focused ROI model

Inputs:

- Monthly request count.
- Average manual triage minutes/request.
- Coordinator hourly cost.
- After-hours requests/month.
- Average avoidable vendor revisit or wrong dispatch cost.

Example formula:

`monthly_time_savings = requests * minutes_saved_per_request / 60 * hourly_cost`

`avoidable_dispatch_savings = prevented_wrong_dispatches * average_trip_cost`

Position the product only when expected monthly value exceeds 3x subscription price.

## Red flags / invalidation

- Managers already force 95%+ of requests through a clean PMS workflow.
- Buyer refuses to pay for audit even after acknowledging time burden.
- Emergency liability concerns cannot be solved with human approval and clear disclaimers.
- Vendor routing is too customized for a repeatable MVP in the chosen segment.

## Evidence to collect

- Before/after triage time on sample requests.
- Number of clarification messages avoided.
- Emergency/urgent misclassification rate in test set.
- Willingness-to-pay quotes.
- Buyer objections by segment.

## Next action checklist

- Build a one-page audit offer using `docs/LANDING_COPY.md`.
- Create a 20-request sample deck with mock tenant messages.
- Contact 30 property managers via local associations, LinkedIn, and cold email.
- Run at least 5 concierge audits before writing production code.
