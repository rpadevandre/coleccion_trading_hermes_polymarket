# Cybersecurity Layer — Property Maintenance Triage

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    - Tenant/vendor/admin role isolation
- Property-level data partitioning
- Secure media upload with file type/size validation
- Signed URLs for tenant photos/videos
- Audit trail for status and vendor assignment changes
- Anti-abuse/rate limits for public tenant forms
- Prompt-injection protection for tenant-provided text/media captions

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
