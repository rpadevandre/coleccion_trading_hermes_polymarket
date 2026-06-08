# Technical Spec — Construction Bid Inbox

This is the canonical required technical specification file for the business folder. It preserves the original `TECH_SPEC.md` content while using the standardized `TECHNICAL_SPEC.md` filename required by the internal business checklist.

## Canonical MVP scope

- Keep this as an internal planning artifact only; no deployment instructions, secrets, or real customer data.
- Split later into frontend, backend, admin, and docs repositories if Andre chooses to upload to GitHub.
- Build the smallest testable workflow around paid validation: one narrow buyer, one painful workflow, one measurable revenue or time-saving metric.
- Require human approval for externally visible AI-generated messages until the product has audited performance data.
- Store only mock/sample data in this repo.

## Original technical notes

# Technical Spec — Construction Bid Inbox Copilot

## Repo pattern

This folder simulates 3 future repos:

- `backend/` — API, data model, automations, integrations.
- `frontend/` — landing/client experience.
- `admin/` — internal control panel.

## Backend initial responsibilities

- Entities and persistence.
- Intake endpoints.
- AI classification/summarization helper.
- Notification/routing placeholders.
- Audit logs.

## Frontend initial responsibilities

- English-first landing page.
- ROI/value calculator where relevant.
- Demo flow pages.
- Waitlist/audit request CTA.

## Admin initial responsibilities

- Dashboard list view.
- Detail pages.
- Configuration/rules UI.
- Status and manual review controls.

