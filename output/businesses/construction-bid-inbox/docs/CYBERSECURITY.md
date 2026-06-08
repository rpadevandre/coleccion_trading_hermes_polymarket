# Cybersecurity Layer — Construction Bid Inbox Copilot

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    - Email ingestion allowlist and attachment scanning
- Document access control by company/project/estimator
- Sensitive bid data encryption at rest
- Audit log for extraction edits and bid/no-bid decisions
- Secure attachment handling; no blind code execution from files
- LLM data boundary: project docs treated as confidential untrusted input
- Least-privilege integrations for email/calendar

    ## Baseline implementation checklist

    - Authentication with secure session handling.
    - RBAC/ABAC depending on tenant and role needs.
    - Input validation at API boundaries.
    - Output encoding in frontend/admin views.
    - CSRF protection where cookie auth is used.
    - CORS allowlist, not wildcard in production.
    - Rate limits and abuse detection for public endpoints.
    - Centralized audit log for sensitive actions.
    - Dependency scanning before release.
    - Separate staging/prod secrets.
