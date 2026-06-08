# Technical Spec — Chiropractic Patient Reactivation Engine

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    - Imports inactive patient CSVs/manual lists
- Segments by recency, visit type and reactivation eligibility
- Drafts safe rebooking/nurture messages for staff approval
- Tracks reply status, booked appointment and no-show outcomes
- Reports recovered revenue and campaign performance

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.
