# Cybersecurity Layer — Restaurant Catering Follow-Up Copilot

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    - RBAC for owner, manager and staff users
- PII minimization for event/customer contact data
- Rate limiting and spam protection on public forms
- Audit log for quote/status changes
- No payment data stored in MVP
- Template approval for outbound messages
- Prompt-injection guardrails for inquiry text

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
