from pathlib import Path
from textwrap import dedent

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')
root.mkdir(parents=True, exist_ok=True)

businesses = {
    'hvac-missed-call-recovery': {
        'name': 'HVAC Missed-Call Recovery',
        'sector': 'Home services / HVAC',
        'buyer': 'Owner/operator or operations manager at 3-15 technician HVAC companies in US/Canada/UK/Australia.',
        'frontend_views': [
            'Landing page with missed-call ROI promise',
            'ROI calculator for missed HVAC calls',
            'Demo call-flow walkthrough',
            'Free missed-call leakage audit form',
            'Pricing/pilot request page',
        ],
        'engine': [
            'Ingests missed call, voicemail, SMS or web form events',
            'Normalizes customer/contact/location/equipment details',
            'Classifies urgency using HVAC-specific rules plus optional LLM summarization',
            'Routes emergencies to on-call contact and non-emergencies to morning queue',
            'Calculates estimated recovered revenue and operational SLA metrics',
        ],
        'admin_views': [
            'Lead recovery dashboard',
            'Emergency lead detail with transcript and summary',
            'Routing rules editor',
            'Service area and business hours settings',
            'Technician/on-call contacts manager',
            'Recovered revenue analytics',
        ],
        'internal_ais': [
            'Triage AI: classifies emergency vs non-emergency',
            'Summary AI: turns transcripts into dispatcher-ready job cards',
            'ROI AI: explains missed-call leakage in plain English',
            'QA AI: flags ambiguous, unsafe or low-confidence conversations',
        ],
        'security': [
            'Role-based access: owner, dispatcher, technician, auditor',
            'PII minimization for phone/address/customer notes',
            'Encrypted env/secrets; no API keys in repo',
            'Audit log for lead changes and routing decisions',
            'Webhook signature verification for telephony/SMS providers',
            'Rate limiting on public intake endpoints',
            'Prompt-injection guardrails: transcripts treated as untrusted data',
        ],
    },
    'property-maintenance-triage': {
        'name': 'Property Maintenance Triage',
        'sector': 'Property management / real estate operations',
        'buyer': 'Small property managers, landlords with 20-300 doors, small multifamily operators.',
        'frontend_views': [
            'Tenant maintenance request landing/form',
            'Photo/video upload guided intake',
            'Request status page',
            'Emergency instructions page',
            'Vendor-facing work order summary page',
        ],
        'engine': [
            'Captures tenant maintenance requests with structured prompts',
            'Requests missing photos/details automatically',
            'Classifies urgency: emergency, urgent, routine, duplicate, incomplete',
            'Maps issue type to vendor category and suggested next action',
            'Generates clean work orders and tenant response drafts',
        ],
        'admin_views': [
            'Maintenance inbox by urgency',
            'Request detail with tenant history and media',
            'Vendor routing board',
            'Property/unit directory',
            'SLA and response-time analytics',
            'Template/rules configuration',
        ],
        'internal_ais': [
            'Maintenance Classifier AI: detects urgency and category',
            'Tenant Clarifier AI: asks for missing context/photos',
            'Vendor Brief AI: creates concise work-order summaries',
            'Duplicate Detector AI: spots repeated issues by unit/property',
        ],
        'security': [
            'Tenant/vendor/admin role isolation',
            'Property-level data partitioning',
            'Secure media upload with file type/size validation',
            'Signed URLs for tenant photos/videos',
            'Audit trail for status and vendor assignment changes',
            'Anti-abuse/rate limits for public tenant forms',
            'Prompt-injection protection for tenant-provided text/media captions',
        ],
    },
    'construction-bid-inbox': {
        'name': 'Construction Bid Inbox Copilot',
        'sector': 'Construction / preconstruction / subcontractors',
        'buyer': 'Subcontractor owner, estimator, preconstruction manager, small GC.',
        'frontend_views': [
            'Product landing for estimators',
            'Bid inbox problem demo',
            'Deadline/addenda extraction demo',
            'Waitlist / request a bid-inbox audit form',
            'ROI page: missed bid deadlines and addenda risk',
        ],
        'engine': [
            'Ingests forwarded bid invite emails and attachments metadata',
            'Extracts bid due dates, pre-bid meetings, RFI deadlines, addenda and contacts',
            'Classifies project fit by trade, location, deadline and scope keywords',
            'Creates estimator task cards and addenda alerts',
            'Generates proposal checklist and response drafts',
        ],
        'admin_views': [
            'Bid pipeline dashboard',
            'Bid invite detail with extracted deadlines',
            'Addenda/change alert board',
            'Estimator assignment view',
            'Project fit rules editor',
            'Submission calendar',
        ],
        'internal_ais': [
            'Bid Parser AI: extracts structured fields from email text/PDF snippets',
            'Fit Scorer AI: ranks opportunities by trade/location/deadline fit',
            'Addenda Watch AI: flags new changes and deadline shifts',
            'Proposal Checklist AI: creates scope-specific next-action lists',
        ],
        'security': [
            'Email ingestion allowlist and attachment scanning',
            'Document access control by company/project/estimator',
            'Sensitive bid data encryption at rest',
            'Audit log for extraction edits and bid/no-bid decisions',
            'Secure attachment handling; no blind code execution from files',
            'LLM data boundary: project docs treated as confidential untrusted input',
            'Least-privilege integrations for email/calendar',
        ],
    },
    'dental-insurance-checklist': {
        'name': 'Dental Insurance Checklist Assistant',
        'sector': 'Dental operations / insurance verification',
        'buyer': 'Dental practice owner, office manager, small DSO operations lead.',
        'frontend_views': [
            'Patient pre-visit intake page',
            'Insurance card/photo upload page',
            'Benefits status page',
            'Treatment estimate explanation page',
            'Practice-facing validation landing',
        ],
        'engine': [
            'Collects patient insurance details before the visit',
            'Generates verification checklist for front desk staff',
            'Tracks missing eligibility/benefits fields',
            'Creates patient-friendly benefit summary drafts',
            'Flags high-risk denial/confusion cases for human review',
        ],
        'admin_views': [
            'Insurance verification queue',
            'Patient verification detail',
            'Missing information tracker',
            'Payer checklist templates',
            'Treatment coordinator notes view',
            'Compliance/audit log',
        ],
        'internal_ais': [
            'Checklist AI: maps payer/procedure context to verification tasks',
            'Patient Explanation AI: drafts plain-English benefit summaries',
            'Risk Flag AI: detects missing fields or denial-risk signals',
            'Office Notes AI: formats PMS-ready human-reviewed notes',
        ],
        'security': [
            'HIPAA-aware architecture assumption before production',
            'No PHI in prompts/logs unless compliant vendor path exists',
            'Strict access roles: front desk, coordinator, manager, auditor',
            'Encrypted storage for insurance documents',
            'Signed uploads and short-lived file access',
            'Audit logs for every patient record access/change',
            'Human-in-the-loop required for benefit/coverage communication',
        ],
    },
    'msp-security-reporting': {
        'name': 'MSP Security Reporting Copilot',
        'sector': 'Managed IT / cybersecurity services',
        'buyer': 'Small MSP owners and vCISO/service delivery leads serving SMB clients.',
        'frontend_views': [
            'Landing page for MSP monthly reporting pain',
            'Sample executive security report preview',
            'Client portal teaser',
            'Free report cleanup/audit request form',
            'Pricing/pilot page',
        ],
        'engine': [
            'Ingests exported alerts, tickets, endpoint/security metrics and manual notes',
            'Normalizes client/month/service categories',
            'Summarizes what happened, what was remediated and what remains risky',
            'Generates client-friendly executive reports and internal action lists',
            'Flags missing evidence, repeated issues and SLA gaps',
        ],
        'admin_views': [
            'Client reporting dashboard',
            'Monthly report builder',
            'Evidence/import review queue',
            'Risk register per client',
            'Template and tone settings',
            'Approval workflow before sending reports',
        ],
        'internal_ais': [
            'Report Writer AI: converts technical noise into executive summaries',
            'Risk Translator AI: explains business impact without fearmongering',
            'Evidence Gap AI: flags missing proof/screenshots/ticket links',
            'Action Plan AI: drafts next-month priorities for the MSP team',
        ],
        'security': [
            'Strong tenant isolation per MSP client',
            'Role-based access: MSP admin, technician, vCISO, client viewer',
            'Encryption at rest for imported reports/tickets',
            'No secrets ingestion; redact keys/tokens/passwords from imported text',
            'Audit logs for report generation, edits and approvals',
            'Approval gate before client-visible reports are sent',
            'Prompt-injection and data-exfiltration guardrails for imported security logs',
        ],
    },
}

for slug, b in businesses.items():
    br = root / slug
    for sub in ['docs', 'frontend/src/views', 'backend/src/modules', 'admin/src/views', 'public-content/en', 'public-content/es']:
        (br / sub).mkdir(parents=True, exist_ok=True)
    if not (br / 'README.md').exists():
        (br / 'README.md').write_text(f"# {b['name']}\n\nInternal scaffold only.\n")
    (br / 'docs' / 'PRODUCT_ARCHITECTURE.md').write_text(dedent(f'''
    # Product Architecture — {b['name']}

    ## Sector

    {b['sector']}

    ## Frontend views

    {chr(10).join('- ' + x for x in b['frontend_views'])}

    ## Backend / motor

    The motor is the operational workflow layer. It does not try to be a generic chatbot; it converts messy inbound information into structured, reviewable, auditable work.

    {chr(10).join('- ' + x for x in b['engine'])}

    ## Admin panel views

    {chr(10).join('- ' + x for x in b['admin_views'])}
    ''').strip() + '\n')
    (br / 'docs' / 'INTERNAL_AI_SYSTEM.md').write_text(dedent(f'''
    # Internal AI System — {b['name']}

    ## Principle

    Internal AI agents support classification, summarization, drafting and decision support. They should not silently take irreversible actions.

    ## Internal AIs

    {chr(10).join('- ' + x for x in b['internal_ais'])}

    ## Human-in-the-loop rules

    - Low confidence outputs require manual review.
    - High-risk decisions require approval.
    - AI-generated external messages are drafts unless explicitly approved by policy.
    - All AI outputs should store source references or explanation notes where possible.

    ## Prompt/data boundary

    User/customer/vendor/tenant/client input is untrusted. It must never be allowed to override system policy, reveal secrets, or trigger unauthorized actions.
    ''').strip() + '\n')
    (br / 'docs' / 'CYBERSECURITY.md').write_text(dedent(f'''
    # Cybersecurity Layer — {b['name']}

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Controls

    {chr(10).join('- ' + x for x in b['security'])}

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
    ''').strip() + '\n')
    (br / 'frontend' / 'VIEWS.md').write_text('# Frontend Views\n\n' + '\n'.join('- ' + x for x in b['frontend_views']) + '\n')
    (br / 'backend' / 'MOTOR.md').write_text('# Backend Motor\n\n' + '\n'.join('- ' + x for x in b['engine']) + '\n')
    (br / 'admin' / 'VIEWS.md').write_text('# Admin Panel Views\n\n' + '\n'.join('- ' + x for x in b['admin_views']) + '\n')
    (br / 'docs' / 'STATUS.md').write_text(dedent(f'''
    # Status — {b['name']}

    ## Current state

    Internal business scaffold expanded with frontend views, backend motor, admin views, internal AI system and cybersecurity layer.

    ## Next build step

    Create lightweight typed models and route/page skeletons only after Andre chooses this business for deeper incubation.
    ''').strip() + '\n')

(root / 'INDEX.md').write_text(dedent('''
# Business Index

## Current target

Have 5 internally complete business folders by around 8pm June 8, with documentation, frontend views, backend motor, admin panel views, internal AI system and cybersecurity layer.

## Businesses

''').lstrip() + '\n'.join([f"- [{b['name']}]({slug}/README.md) — docs/frontend/backend/admin + AI/cybersecurity layer" for slug, b in businesses.items()]) + '\n')

readme = root / 'README.md'
existing = readme.read_text() if readme.exists() else ''
readme.write_text(dedent('''
# Business Incubation Output

Carpeta interna para que AION prepare negocios completos dentro del repo actual antes de que Andre los suba a GitHub como repos privados o separados.

## Reglas

- No deployar.
- No tocar Nexbody.
- No usar datos reales de clientes.
- Public assets EN-first; adaptación ES después.
- Cada negocio debe tener documentación, frontend, backend, panel de control/admin, IAs internas y capa de ciberseguridad.

## Estructura por negocio

```text
output/businesses/<business-slug>/
  README.md
  docs/
    BUSINESS_PLAN.md
    TARGET_AUDIENCE.md
    BRAND_KIT.md
    TECH_SPEC.md
    PRODUCT_ARCHITECTURE.md
    INTERNAL_AI_SYSTEM.md
    CYBERSECURITY.md
    VALIDATION_PLAN.md
    STATUS.md
  frontend/
    README.md
    VIEWS.md
  backend/
    README.md
    MOTOR.md
  admin/
    README.md
    VIEWS.md
  public-content/en/
  public-content/es/
```

## Negocios iniciales

1. `hvac-missed-call-recovery`
2. `property-maintenance-triage`
3. `construction-bid-inbox`
4. `dental-insurance-checklist`
5. `msp-security-reporting`
''').strip() + '\n')

print('enriched', len(businesses), 'businesses under', root)
for slug in businesses:
    print(slug)
