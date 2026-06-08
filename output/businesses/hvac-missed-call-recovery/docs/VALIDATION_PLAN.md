# Validation Plan — HVAC Missed-Call Recovery

## Validation thesis

HVAC contractors will pay for a missed-call recovery system if it proves that unanswered calls are becoming booked jobs faster than a dispatcher-only workflow. The validation path should prioritize English-speaking markets with high emergency-ticket value: US, Canada, UK, and Australia.

## Target prospects

- 3–15 technician HVAC companies.
- Owner still involved in dispatch or after-hours escalation.
- Existing phone stack with call logs: CallRail, OpenPhone, RingCentral, Twilio, ServiceTitan phones, Jobber, or similar.
- Runs Google Local Services/paid search and therefore feels lead-waste pain.

## Money-focused audit offer

“Send us your last 30 days of aggregate call stats — total calls, missed calls, after-hours missed calls, average booked job value, and rough booking rate. We’ll return a missed-call leakage estimate and a callback workflow you can test for two weeks.”

No real call recordings or customer data should be stored in this repo. For live validation, use prospect-provided aggregate counts or sanitized exports only.

## 7-day validation sprint

1. Build a mock ROI calculator with editable assumptions.
2. Create a one-page demo showing missed call → SMS acknowledgement → dispatcher queue → booked job.
3. Identify 30 HVAC companies in English-speaking metros with visible emergency/after-hours messaging.
4. Send owner/operator outreach offering a free missed-call leakage audit.
5. Ask discovery questions:
   - How many calls do you miss during peak season?
   - Who checks voicemail after hours?
   - What is an emergency call worth if it books?
   - What happens when a caller texts back?
   - Would you pay for recovered booked jobs, a flat monthly fee, or both?
6. Request a paid pilot only after the owner confirms the pain and provides baseline numbers.
7. Track reply rate, audit requests, paid pilot intent, and actual data access.

## Pilot pricing hypothesis

- Setup: $500–$1,500 for call-flow mapping, templates, and routing rules.
- Monthly: $300–$900 for small shops, tied to missed-call volume.
- Performance add-on: optional recovered booking bonus only if attribution is clean.

## Success metrics

- 10%+ positive reply rate from owner/operator outreach.
- 5+ audit requests from 30–50 prospects.
- 2+ prospects willing to share aggregate call stats.
- 1 paid pilot or signed LOI with clear baseline: missed calls/month, callback SLA, booked jobs recovered.

## Kill/pivot signals

- Shops already have 24/7 call center coverage and do not care about additional recovery.
- Owners will not share even aggregate call data.
- Missed-call count is too low to justify monthly pricing.
- Integration complexity blocks a manual concierge pilot.

## Validation guardrails

- Do not promise fixed revenue recovery.
- Do not deploy production integrations during this cron work.
- Do not collect real customer names, phone numbers, recordings, or addresses for repo artifacts.
