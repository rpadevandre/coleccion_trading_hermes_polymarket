# Cybersecurity Layer — B2B Podcast Repurposing System

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    - Private transcript storage and workspace isolation
- Role-based access for owner, editor and client
- No publishing without explicit approval
- Source attribution maintained to avoid context drift
- Redaction workflow for confidential client/company names
- Rate limits on uploads/generation endpoints
- Prompt-injection safeguards for transcript content

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
