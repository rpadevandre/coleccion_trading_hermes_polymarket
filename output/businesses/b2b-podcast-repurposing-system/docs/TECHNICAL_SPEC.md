# Technical Spec — B2B Podcast Repurposing System

This is the canonical required technical specification file for the business folder. It preserves the original `TECH_SPEC.md` content while using the standardized `TECHNICAL_SPEC.md` filename required by the internal business checklist.

## Canonical MVP scope

- Keep this as an internal planning artifact only; no deployment instructions, secrets, or real customer data.
- Split later into frontend, backend, admin, and docs repositories if Andre chooses to upload to GitHub.
- Build the smallest testable workflow around paid validation: one narrow buyer, one painful workflow, one measurable revenue or time-saving metric.
- Require human approval for externally visible AI-generated messages until the product has audited performance data.
- Store only mock/sample data in this repo.

## Original technical notes

# Technical Spec — B2B Podcast Repurposing System

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    - Ingests transcript text or notes
- Extracts themes, claims, stories, objections and quotable moments
- Generates channel-specific drafts for LinkedIn, X and email
- Scores content for clarity, novelty and audience fit
- Builds a weekly publishing queue

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.

