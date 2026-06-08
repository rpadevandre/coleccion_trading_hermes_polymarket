# Cybersecurity Layer — Dental Insurance Checklist Assistant

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    - HIPAA-aware architecture assumption before production
- No PHI in prompts/logs unless compliant vendor path exists
- Strict access roles: front desk, coordinator, manager, auditor
- Encrypted storage for insurance documents
- Signed uploads and short-lived file access
- Audit logs for every patient record access/change
- Human-in-the-loop required for benefit/coverage communication

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
