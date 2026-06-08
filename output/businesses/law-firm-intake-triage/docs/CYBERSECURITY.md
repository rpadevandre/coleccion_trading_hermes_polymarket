# Cybersecurity Layer — Law Firm Intake Triage

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    - Attorney-client confidentiality assumptions from day zero
- Strict RBAC for attorney, intake, admin and auditor roles
- No legal advice generated; informational summaries only
- Consent and disclaimer capture before intake submission
- Encrypted storage for sensitive intake data
- Audit logs for every inquiry access/change
- Prompt-injection protection for client-submitted narratives

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
