# Cybersecurity Layer — MSP Security Reporting Copilot

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    - Strong tenant isolation per MSP client
- Role-based access: MSP admin, technician, vCISO, client viewer
- Encryption at rest for imported reports/tickets
- No secrets ingestion; redact keys/tokens/passwords from imported text
- Audit logs for report generation, edits and approvals
- Approval gate before client-visible reports are sent
- Prompt-injection and data-exfiltration guardrails for imported security logs

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
