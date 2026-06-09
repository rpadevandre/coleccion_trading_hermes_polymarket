# Restaurant Catering Followup — FastAPI Backend

    This is the first executable backend scaffold for **Restaurant Catering Followup**.

    ## Current status

    - Framework: Python + FastAPI.
    - Database: MongoDB planned, **not connected yet**.
    - Current persistence: in-memory repository for local prototype validation.
    - Public API docs: `/docs` when running locally.

    ## Why no database connection yet

    Andre specified that each business will use MongoDB later, but the current
    step should advance backend structure without connecting databases. This
    keeps secrets, schemas, indexes, and retention policies out of the repo until
    the product direction is confirmed.

    ## Run locally

    ```bash
    cd output/businesses/restaurant-catering-followup/backend
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8000
    ```

    Open:

    ```text
    http://localhost:8000/docs
    http://localhost:8000/health
    http://localhost:8000/meta
    ```

    ## Core endpoints

    ```text
    GET  /health
    GET  /meta
    POST /intakes
    GET  /intakes
    GET  /intakes/{intake_id}
    POST /assessments/score
    GET  /admin/queue
    ```

    ## Planned Mongo collections

    ```text
    database: restaurant_catering_followup
    intakes: catering_opportunity_intakes
    assessments: catering_opportunity_assessments
    audit_events: audit_events
    ```

    ## Business modules represented

    - `CateringInquiryIntakeService`
- `EventDetailsExtractor`
- `QuoteChecklistBuilder`
- `FollowupReminderEngine`
- `BookedRevenueTracker`

    ## Next backend step

    1. Add real unit tests with `pytest` + FastAPI `TestClient`.
    2. Add Mongo repository behind the current repository interface using Motor.
    3. Define Mongo indexes and retention rules.
    4. Add auth/tenant boundaries before any real customer data.
