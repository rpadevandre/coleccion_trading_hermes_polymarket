# Validation Plan — Chiropractic Patient Reactivation Engine

## Validation thesis

Chiropractic clinics will pay for reactivation if the system proves it can safely convert inactive patients into attended appointments and recovered revenue without creating compliance, reputation, or staff-overload risk.

## Target prospects

- Solo to mid-sized chiropractic clinics in English-speaking markets.
- Clinics with 500+ historical patients and inconsistent recall workflows.
- Owners who are spending on new-patient ads but lack a measured inactive-patient campaign.
- Office managers who can approve messages and track booked/attended appointments.

## Money-focused audit offer

“Before buying more new-patient ads, estimate the revenue sitting in your inactive patient list. We’ll use aggregate numbers only: inactive patients by recency, reachable percentage, average visit value, and current recall process.”

No real patient data, PHI, diagnoses, or phone numbers belong in this repo. Live validation should start with aggregate counts and synthetic demos.

## 7-day validation sprint

1. Create a mock CSV with synthetic inactive patients across 90-day, 6-month, and 12-month segments.
2. Build a demo walkthrough: import → eligibility suppressions → message drafts → staff approval → booked/attended report.
3. Identify 30 chiropractic clinics or clinic-marketing agencies in US/Canada/UK/Australia.
4. Send a problem-first note about recovering existing patient revenue before increasing ad spend.
5. Discovery questions:
   - How large is your inactive patient list?
   - Who handles recall today, and how often?
   - What percentage of reactivated patients attend at least one appointment?
   - What compliance/consent rules does your clinic follow for SMS/email?
   - Would a staff-approved AI drafting queue save time or create risk?
6. Ask for a paid mock audit or LOI only after confirming list size, staff bandwidth, and compliance appetite.
7. Track reply rate, booked discovery calls, aggregate-data availability, and willingness to pay.

## Pilot pricing hypothesis

- Setup: $750–$2,000 for segmentation, templates, suppression rules, and staff workflow.
- Monthly: $300–$1,000 depending on patient list size and campaign cadence.
- Optional agency package for healthcare marketers managing multiple clinics.

## Success metrics

- 8%+ positive reply rate from clinic owners/managers.
- 5+ clinics agree inactive-patient revenue is a current pain.
- 2+ clinics willing to run an aggregate mock audit.
- 1 paid pilot/LOI with explicit compliance approval path and staff owner.

## Kill/pivot signals

- Clinics cannot or will not approve any patient outreach workflow.
- Inactive list size is too small to support a meaningful ROI case.
- Compliance concerns prevent even staff-approved draft workflows.
- Existing EHR/practice-management system already performs recall well enough.

## Validation guardrails

- Do not ask for PHI during early validation.
- Do not generate clinical advice or treatment recommendations.
- Do not message patients without clinic approval, opt-out handling, and compliance review.
