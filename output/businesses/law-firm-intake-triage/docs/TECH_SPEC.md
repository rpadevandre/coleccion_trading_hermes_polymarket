# Technical Spec — Law Firm Intake Triage

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    - Captures inquiry details with practice-area-specific questions
- Classifies practice area and urgency
- Flags missing facts, conflict-check needs and jurisdiction issues for human review
- Generates attorney-ready intake summaries
- Routes leads to intake specialist or attorney based on rules

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.
