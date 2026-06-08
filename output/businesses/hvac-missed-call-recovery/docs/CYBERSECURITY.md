# Cybersecurity Layer — HVAC Missed-Call Recovery

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    - Role-based access: owner, dispatcher, technician, auditor
- PII minimization for phone/address/customer notes
- Encrypted env/secrets; no API keys in repo
- Audit log for lead changes and routing decisions
- Webhook signature verification for telephony/SMS providers
- Rate limiting on public intake endpoints
- Prompt-injection guardrails: transcripts treated as untrusted data

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
