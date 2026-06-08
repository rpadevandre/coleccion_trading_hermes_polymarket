# Technical Spec — Med Spa Lead Recovery

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    - Ingests missed calls, web forms, SMS and manual DM exports
- Normalizes lead source, treatment interest, budget/timing and contact details
- Classifies lead temperature: hot consult, nurture, low intent, spam, needs human review
- Drafts compliant follow-up messages without making medical claims
- Tracks booked consults, no-shows and estimated recovered revenue

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.
