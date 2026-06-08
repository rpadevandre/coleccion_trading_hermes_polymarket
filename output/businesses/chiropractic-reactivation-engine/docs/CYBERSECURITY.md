# Cybersecurity Layer — Chiropractic Patient Reactivation Engine

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    - Healthcare privacy-aware architecture; avoid PHI in non-compliant tools
- Human approval before patient messages
- Role separation for owner, coordinator and marketer
- CSV import validation and secure deletion workflow
- Audit logs for patient data access and campaign actions
- Opt-out tracking and suppression lists
- Prompt-injection safeguards for patient replies

    ## Baseline implementation checklist

    - Authentication with secure session handling.
    - RBAC/ABAC depending on tenant and role needs.
    - Input validation at all API boundaries.
    - Output encoding in frontend/admin views.
    - CSRF protection where cookie auth is used.
    - CORS allowlist, not wildcard in production.
    - Rate limits and abuse detection for public endpoints.
    - Centralized audit log for sensitive actions.
    - Dependency scanning before release.
    - Separate staging/prod secrets.
    - LLM prompt-injection and data-exfiltration tests before launch.
