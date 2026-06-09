# Dental Insurance Checklist — Admin Panel Frontend

    This folder now contains a lightweight operator/admin panel prototype for **Dental Insurance Checklist**.

    ## Current status

    - Frontend type: dependency-free HTML/CSS/JS admin panel.
    - Backend target: local FastAPI app under `../backend`.
    - Database: none connected; backend uses in-memory repository until MongoDB is approved.
    - Purpose: let Andre inspect the admin workflow for each incubated business from GitHub and run it locally without a build step.

    ## Files

    ```text
    index.html
    styles.css
    app.js
    README.md
    ROUTES.md
    VIEWS.md
    ```

    ## Run locally

    Terminal 1:

    ```bash
    cd output/businesses/dental-insurance-checklist/backend
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8000
    ```

    Terminal 2:

    ```bash
    cd output/businesses/dental-insurance-checklist/admin
    python -m http.server 4173
    ```

    Open:

    ```text
    http://localhost:4173
    ```

    ## Admin views represented

    - Verification Cases
- Checklist Builder
- Policy Summary
- Compliance Guard
- Audit Trail

    ## Connected API actions

    ```text
    GET  /health
    GET  /meta
    POST /intakes
    POST /assessments/score
    GET  /admin/queue
    ```

    ## Next step

    Once a business is chosen as the real MVP, replace this static prototype with either:

    - a React/Vite admin app, or
    - a shared admin shell package reused across all businesses.
