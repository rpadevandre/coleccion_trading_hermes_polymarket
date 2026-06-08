# Cybersecurity Layer — Med Spa Lead Recovery

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    - Role-based access for owner, front desk, provider and marketer
- PII minimization for lead/contact data
- No medical diagnosis or treatment claims generated automatically
- Message approval workflow before external sending
- Audit log for lead edits, message approvals and status changes
- Rate limits and spam filtering on public lead forms
- Prompt-injection guardrails for DM/form content

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
