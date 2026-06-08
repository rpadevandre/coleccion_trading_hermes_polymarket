# Technical Spec — Restaurant Catering Follow-Up Copilot

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    - Captures catering inquiries from form/email/manual entry
- Extracts event date, guest count, location, budget, menu interest and constraints
- Classifies lead readiness and missing information
- Drafts staff-approved follow-ups and quote request checklists
- Tracks status: new, contacted, quoted, booked, lost

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.
