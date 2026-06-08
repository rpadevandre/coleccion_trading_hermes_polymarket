from pathlib import Path
from textwrap import dedent

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')
root.mkdir(parents=True, exist_ok=True)

new_businesses = {
    'med-spa-lead-recovery': {
        'name': 'Med Spa Lead Recovery',
        'sector': 'Med spa / aesthetics clinics',
        'score': '73/90',
        'buyer': 'Med spa owner, clinic manager, aesthetics practice operator in US/Canada/UK/Australia.',
        'user': 'Front desk, sales coordinator, injector/aesthetician, owner.',
        'problem': 'Med spas lose high-value consults when Instagram DMs, missed calls, form leads and SMS follow-ups are scattered or slow.',
        'offer': 'AI-assisted lead recovery and consult booking workflow for med spas: captures inbound leads, qualifies intent, drafts follow-ups, books consults and reports lost/recovered revenue.',
        'headline': 'Turn missed med spa leads into booked consults.',
        'es': 'Convierte leads perdidos de med spa en consultas agendadas.',
        'frontend_views': [
            'Landing page for med spa lead leakage',
            'Lead value / missed consult ROI calculator',
            'Instagram DM-to-consult demo flow',
            'Free lead follow-up audit form',
            'Pilot/pricing request page',
        ],
        'engine': [
            'Ingests missed calls, web forms, SMS and manual DM exports',
            'Normalizes lead source, treatment interest, budget/timing and contact details',
            'Classifies lead temperature: hot consult, nurture, low intent, spam, needs human review',
            'Drafts compliant follow-up messages without making medical claims',
            'Tracks booked consults, no-shows and estimated recovered revenue',
        ],
        'admin_views': [
            'Lead recovery dashboard',
            'Lead detail with source, treatment interest and follow-up history',
            'Follow-up queue',
            'Treatment/service settings',
            'Message template approval view',
            'Recovered consult analytics',
        ],
        'internal_ais': [
            'Lead Intent AI: classifies buying intent and treatment interest',
            'Follow-up Draft AI: writes human-approved consult booking messages',
            'Compliance Guard AI: flags risky medical/guarantee language',
            'Revenue Leak AI: estimates missed consult value by source',
        ],
        'security': [
            'Role-based access for owner, front desk, provider and marketer',
            'PII minimization for lead/contact data',
            'No medical diagnosis or treatment claims generated automatically',
            'Message approval workflow before external sending',
            'Audit log for lead edits, message approvals and status changes',
            'Rate limits and spam filtering on public lead forms',
            'Prompt-injection guardrails for DM/form content',
        ],
        'palette': ['#4C1D95 luxury violet', '#F472B6 aesthetic pink', '#FDF2F8 soft background', '#111827 text', '#D97706 premium gold'],
    },
    'law-firm-intake-triage': {
        'name': 'Law Firm Intake Triage',
        'sector': 'Small law firms / legal intake',
        'score': '70/90',
        'buyer': 'Small law firm owner, managing attorney, intake manager, legal marketing agency serving firms.',
        'user': 'Intake specialist, paralegal, attorney reviewer, receptionist.',
        'problem': 'Small law firms lose potential cases because intake is slow, inconsistent, after-hours calls are missed, and weak leads waste attorney time.',
        'offer': 'AI-assisted legal intake triage: structured intake, practice-area routing, conflict/checklist prompts, lead quality scoring and attorney-ready summaries.',
        'headline': 'Turn messy legal inquiries into attorney-ready intake summaries.',
        'es': 'Convierte consultas legales desordenadas en resúmenes listos para abogado.',
        'frontend_views': [
            'Landing page for law firm intake bottlenecks',
            'Practice-area intake form demo',
            'After-hours inquiry capture page',
            'Case quality scoring explainer',
            'Consultation request CTA',
        ],
        'engine': [
            'Captures inquiry details with practice-area-specific questions',
            'Classifies practice area and urgency',
            'Flags missing facts, conflict-check needs and jurisdiction issues for human review',
            'Generates attorney-ready intake summaries',
            'Routes leads to intake specialist or attorney based on rules',
        ],
        'admin_views': [
            'Intake queue by urgency/practice area',
            'Lead detail and attorney summary',
            'Practice area routing rules',
            'Conflict checklist status',
            'Source/channel analytics',
            'Rejected/unqualified lead review',
        ],
        'internal_ais': [
            'Practice Area AI: categorizes inquiry type',
            'Intake Summary AI: structures facts into attorney-readable notes',
            'Risk/Compliance AI: flags legal advice risk and missing disclaimers',
            'Lead Quality AI: scores urgency, fit and potential value',
        ],
        'security': [
            'Attorney-client confidentiality assumptions from day zero',
            'Strict RBAC for attorney, intake, admin and auditor roles',
            'No legal advice generated; informational summaries only',
            'Consent and disclaimer capture before intake submission',
            'Encrypted storage for sensitive intake data',
            'Audit logs for every inquiry access/change',
            'Prompt-injection protection for client-submitted narratives',
        ],
        'palette': ['#111827 legal charcoal', '#1D4ED8 trust blue', '#F8FAFC clean surface', '#92400E formal gold', '#7F1D1D risk red'],
    },
    'chiropractic-reactivation-engine': {
        'name': 'Chiropractic Patient Reactivation Engine',
        'sector': 'Chiropractic / local healthcare marketing',
        'score': '67/90',
        'buyer': 'Chiropractic clinic owner, office manager, clinic marketing agency.',
        'user': 'Front desk, patient coordinator, clinic owner.',
        'problem': 'Chiropractic clinics have inactive patient lists but inconsistent reactivation campaigns, weak follow-up and little visibility into rebooked revenue.',
        'offer': 'AI-assisted patient reactivation workflow: segment inactive patients, draft compliant rebooking messages, track replies, appointments and recovered revenue.',
        'headline': 'Reactivate inactive patients without sounding like spam.',
        'es': 'Reactiva pacientes inactivos sin sonar como spam.',
        'frontend_views': [
            'Landing page for patient reactivation',
            'Recovered appointment value calculator',
            'Campaign preview/demo',
            'Free inactive-list audit request',
            'Pilot signup page',
        ],
        'engine': [
            'Imports inactive patient CSVs/manual lists',
            'Segments by recency, visit type and reactivation eligibility',
            'Drafts safe rebooking/nurture messages for staff approval',
            'Tracks reply status, booked appointment and no-show outcomes',
            'Reports recovered revenue and campaign performance',
        ],
        'admin_views': [
            'Inactive patient segments',
            'Campaign builder and approval queue',
            'Reply tracking inbox',
            'Appointment recovery analytics',
            'Message template library',
            'Compliance review log',
        ],
        'internal_ais': [
            'Segmentation AI: groups inactive patients by likely reactivation path',
            'Message Draft AI: writes gentle rebooking messages',
            'Compliance Guard AI: avoids diagnosis/treatment guarantees',
            'Performance Insight AI: explains which segments/messages work',
        ],
        'security': [
            'Healthcare privacy-aware architecture; avoid PHI in non-compliant tools',
            'Human approval before patient messages',
            'Role separation for owner, coordinator and marketer',
            'CSV import validation and secure deletion workflow',
            'Audit logs for patient data access and campaign actions',
            'Opt-out tracking and suppression lists',
            'Prompt-injection safeguards for patient replies',
        ],
        'palette': ['#064E3B wellness green', '#10B981 mint', '#ECFDF5 soft background', '#1F2937 text', '#F59E0B action amber'],
    },
    'restaurant-catering-followup': {
        'name': 'Restaurant Catering Follow-Up Copilot',
        'sector': 'Restaurants / catering sales',
        'score': '66/90',
        'buyer': 'Restaurant owner/operator, catering manager, multi-location local restaurant group.',
        'user': 'Catering manager, front-of-house manager, owner.',
        'problem': 'Restaurants miss catering revenue when inquiries from forms, calls, DMs and emails are not followed up quickly or consistently.',
        'offer': 'AI-assisted catering lead follow-up: captures event details, drafts quotes/follow-ups, reminds staff and tracks booked catering revenue.',
        'headline': 'Stop letting catering inquiries die in the inbox.',
        'es': 'Deja de perder solicitudes de catering en el inbox.',
        'frontend_views': [
            'Landing page for catering revenue recovery',
            'Event inquiry form demo',
            'Catering revenue calculator',
            'Quote/follow-up workflow preview',
            'Free catering inbox audit CTA',
        ],
        'engine': [
            'Captures catering inquiries from form/email/manual entry',
            'Extracts event date, guest count, location, budget, menu interest and constraints',
            'Classifies lead readiness and missing information',
            'Drafts staff-approved follow-ups and quote request checklists',
            'Tracks status: new, contacted, quoted, booked, lost',
        ],
        'admin_views': [
            'Catering leads board',
            'Lead detail with event requirements',
            'Follow-up/reminder queue',
            'Menu/package settings',
            'Quote status tracker',
            'Booked/lost revenue analytics',
        ],
        'internal_ais': [
            'Event Details AI: extracts structured event data',
            'Follow-up AI: drafts timely catering replies',
            'Quote Checklist AI: flags missing quote inputs',
            'Revenue Insight AI: tracks lost/booked catering value',
        ],
        'security': [
            'RBAC for owner, manager and staff users',
            'PII minimization for event/customer contact data',
            'Rate limiting and spam protection on public forms',
            'Audit log for quote/status changes',
            'No payment data stored in MVP',
            'Template approval for outbound messages',
            'Prompt-injection guardrails for inquiry text',
        ],
        'palette': ['#7C2D12 warm food brown', '#EA580C orange', '#FFF7ED cream', '#1F2937 text', '#16A34A booked green'],
    },
    'b2b-podcast-repurposing-system': {
        'name': 'B2B Podcast Repurposing System',
        'sector': 'B2B content marketing / founder-led media',
        'score': '65/90',
        'buyer': 'B2B SaaS founder, agency owner, consultant, podcast host, content lead.',
        'user': 'Founder, marketer, editor, social media assistant.',
        'problem': 'B2B founders record podcasts or calls but fail to turn them into consistent LinkedIn/X/email content because repurposing is time-consuming.',
        'offer': 'AI-assisted repurposing workflow: transcript ingestion, idea extraction, LinkedIn posts, X threads, newsletter drafts, clip scripts and content calendar.',
        'headline': 'Turn one B2B conversation into a week of sharp content.',
        'es': 'Convierte una conversación B2B en una semana de contenido potente.',
        'frontend_views': [
            'Landing page for podcast/content repurposing',
            'Before/after content demo',
            'Transcript upload demo',
            'Content calendar preview',
            'Free episode repurpose audit CTA',
        ],
        'engine': [
            'Ingests transcript text or notes',
            'Extracts themes, claims, stories, objections and quotable moments',
            'Generates channel-specific drafts for LinkedIn, X and email',
            'Scores content for clarity, novelty and audience fit',
            'Builds a weekly publishing queue',
        ],
        'admin_views': [
            'Content source library',
            'Draft generation workspace',
            'Channel calendar',
            'Voice/tone settings',
            'Approval/editing queue',
            'Performance notes dashboard',
        ],
        'internal_ais': [
            'Insight Extractor AI: pulls useful business ideas from transcripts',
            'Channel Writer AI: adapts content for LinkedIn/X/email',
            'Voice Guard AI: keeps founder style and removes generic AI tone',
            'Content Strategist AI: suggests sequence and calendar placement',
        ],
        'security': [
            'Private transcript storage and workspace isolation',
            'Role-based access for owner, editor and client',
            'No publishing without explicit approval',
            'Source attribution maintained to avoid context drift',
            'Redaction workflow for confidential client/company names',
            'Rate limits on uploads/generation endpoints',
            'Prompt-injection safeguards for transcript content',
        ],
        'palette': ['#0F172A creator navy', '#8B5CF6 creative purple', '#06B6D4 signal cyan', '#F8FAFC surface', '#111827 text'],
    },
}

common_files = ['BUSINESS_PLAN.md','TARGET_AUDIENCE.md','BRAND_KIT.md','TECH_SPEC.md','PRODUCT_ARCHITECTURE.md','INTERNAL_AI_SYSTEM.md','CYBERSECURITY.md','VALIDATION_PLAN.md','STATUS.md','LANDING_COPY.md','OUTREACH.md','DATA_MODEL.md','API_CONTRACT.md','ADMIN_OPERATIONS.md']

for slug, b in new_businesses.items():
    br = root / slug
    for sub in ['docs', 'frontend/src/views', 'backend/src/modules', 'admin/src/views', 'public-content/en', 'public-content/es']:
        (br / sub).mkdir(parents=True, exist_ok=True)

    (br / 'README.md').write_text(dedent(f'''
    # {b['name']}

    **Score:** {b['score']}
    **Sector:** {b['sector']}

    ## English-first positioning

    {b['headline']}

    ## Spanish adaptation

    {b['es']}

    ## Target buyer

    {b['buyer']}

    ## Target user

    {b['user']}

    ## Problem

    {b['problem']}

    ## Offer v0

    {b['offer']}

    ## Folder map

    - `docs/` — business, audience, brand, validation, technical, AI and cybersecurity specs.
    - `frontend/` — landing/client app scaffold and views.
    - `backend/` — API/services/motor scaffold.
    - `admin/` — control panel scaffold and operations.
    - `public-content/` — build-in-public content EN/ES.

    ## Current status

    Internal scaffold only. No deploy. No GitHub publication yet.
    ''').strip() + '\n')

    (br/'docs'/'BUSINESS_PLAN.md').write_text(dedent(f'''
    # Business Plan — {b['name']}

    ## Goal

    Build a small, monetizable AI workflow product/service for an English-speaking market with clear willingness to pay.

    ## Target buyer

    {b['buyer']}

    ## Target user

    {b['user']}

    ## Pain

    {b['problem']}

    ## Offer

    {b['offer']}

    ## Revenue model hypothesis

    - Paid pilot / setup fee: $300-$2,000 depending on niche and implementation effort.
    - Monthly subscription/support: $99-$799 depending on volume, seats and business value.
    - Done-for-you onboarding before pure SaaS.

    ## Why this can make money

    The product is not positioned as generic AI. It is positioned as revenue recovery, labor savings, operational clarity or client-retention support for buyers who already spend money to solve the underlying problem.

    ## Validation gate

    Do not overbuild until there is at least one of:

    - 2 discovery calls with target buyers.
    - 1 paid pilot or strong intent-to-pay signal.
    - 5+ meaningful replies from outbound/build-in-public.
    - 1 operator willing to test a fake/manual MVP.
    ''').strip() + '\n')

    (br/'docs'/'TARGET_AUDIENCE.md').write_text(dedent(f'''
    # Target Audience — {b['name']}

    ## Buyer

    {b['buyer']}

    ## User

    {b['user']}

    ## English-speaking market first

    US/Canada/UK/Australia buyers are prioritized because they tend to have higher labor costs, stronger SaaS buying culture, clearer willingness to pay for operational tools, and easier USD pricing.

    ## Spanish adaptation

    Spanish copy can support bilingual operators and LATAM/España content, but public positioning should be written natively in English first.
    ''').strip() + '\n')

    (br/'docs'/'BRAND_KIT.md').write_text(dedent(f'''
    # Brand Kit — {b['name']}

    ## Positioning line

    **EN:** {b['headline']}

    **ES:** {b['es']}

    ## Tone

    Practical, operational, specific, ROI-aware, trustworthy, not hypey.

    ## Palette

    {chr(10).join('- ' + c for c in b['palette'])}

    ## Messaging rule

    Lead with the expensive operational problem. Mention AI as the engine, not as the main category.
    ''').strip() + '\n')

    (br/'docs'/'TECH_SPEC.md').write_text(dedent(f'''
    # Technical Spec — {b['name']}

    ## Future repo split

    - `<slug>-frontend` — public landing and client-facing views.
    - `<slug>-backend` — API, business motor, integrations, AI orchestration, audit logs.
    - `<slug>-admin` — internal/admin control panel.
    - `<slug>-os` — strategy/docs/brand/distribution hub if split later.

    ## Backend responsibilities

    {chr(10).join('- ' + x for x in b['engine'])}

    ## MVP data path

    1. Inbound event/intake.
    2. Validation and normalization.
    3. AI-assisted classification/summarization.
    4. Human review/approval where needed.
    5. Operational routing or follow-up.
    6. Status/metric update.
    7. Audit log write.
    ''').strip() + '\n')

    (br/'docs'/'PRODUCT_ARCHITECTURE.md').write_text(dedent(f'''
    # Product Architecture — {b['name']}

    ## Frontend views

    {chr(10).join('- ' + x for x in b['frontend_views'])}

    ## Backend / motor

    The motor converts messy inbound information into structured, reviewable, auditable work. It should make operators faster, not silently replace judgment.

    {chr(10).join('- ' + x for x in b['engine'])}

    ## Admin panel views

    {chr(10).join('- ' + x for x in b['admin_views'])}
    ''').strip() + '\n')

    (br/'docs'/'INTERNAL_AI_SYSTEM.md').write_text(dedent(f'''
    # Internal AI System — {b['name']}

    ## Principle

    Internal AIs classify, summarize, draft, prioritize and explain. They do not silently take irreversible or high-risk actions.

    ## Internal AIs

    {chr(10).join('- ' + x for x in b['internal_ais'])}

    ## Human-in-the-loop rules

    - Low-confidence outputs require manual review.
    - Outbound messages require approval unless explicitly configured otherwise.
    - High-risk/compliance-sensitive content stays draft-only.
    - AI outputs should preserve source references where possible.

    ## Prompt/data boundary

    Customer/user input is untrusted and cannot override system policy, reveal secrets, change permissions, or trigger unauthorized actions.
    ''').strip() + '\n')

    (br/'docs'/'CYBERSECURITY.md').write_text(dedent(f'''
    # Cybersecurity Layer — {b['name']}

    ## Security goals

    - Protect customer/business data.
    - Prevent unauthorized admin access.
    - Keep secrets out of source control.
    - Treat all external content as untrusted.
    - Maintain auditability of operational decisions.

    ## Business-specific controls

    {chr(10).join('- ' + x for x in b['security'])}

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
    ''').strip() + '\n')

    (br/'docs'/'VALIDATION_PLAN.md').write_text(dedent(f'''
    # Validation Plan — {b['name']}

    ## Before building deeply

    1. Create a fake/manual MVP demo using sample data.
    2. Identify 20 target prospects in the English-speaking market.
    3. Send short problem-first outreach.
    4. Ask for discovery calls or a free audit.
    5. Measure replies, calls, pain confirmation and willingness to pay.

    ## Success signal

    A target buyer says: “I have this problem, I understand why it costs money, and I would test/pay for this.”

    ## Kill/Pivot signal

    No replies, no urgency, buyers already solved it cheaply, or compliance/ops complexity blocks a fast pilot.
    ''').strip() + '\n')

    (br/'docs'/'STATUS.md').write_text(dedent(f'''
    # Status — {b['name']}

    Internal business scaffold created with docs, frontend views, backend motor, admin panel views, internal AI system and cybersecurity layer.

    ## Next build step

    Create lightweight API/data model/page skeletons only if Andre selects this business for deeper repo split.
    ''').strip() + '\n')

    (br/'docs'/'LANDING_COPY.md').write_text(dedent(f'''
    # Landing Copy — {b['name']}

    ## Hero

    {b['headline']}

    ## Subheadline

    {b['offer']}

    ## CTA

    Get a free workflow audit.

    ## ES adaptation

    {b['es']}
    ''').strip() + '\n')

    (br/'docs'/'OUTREACH.md').write_text(dedent(f'''
    # Outreach — {b['name']}

    ## Cold email v0

    Subject: quick question about {b['sector'].split('/')[0].strip()} operations

    Hi {{first_name}},

    I’m building a small workflow for teams dealing with this problem:

    > {b['problem']}

    The idea is simple: {b['offer']}

    Not selling a full platform yet — I’m looking for 10 operators to sanity-check whether this is painful enough to pay for.

    Would a 15-minute call next week be unreasonable?

    — Andre
    ''').strip() + '\n')

    (br/'docs'/'DATA_MODEL.md').write_text(dedent('''
    # Data Model

    ## Core entities

    - Account / Tenant
    - User
    - Role
    - InboundItem
    - Classification
    - AIOutput
    - ReviewDecision
    - WorkflowStatus
    - AuditEvent
    - MetricSnapshot

    ## Notes

    Keep the MVP simple. Prefer SQLite/Postgres-compatible relational modeling and add integrations later.
    ''').strip() + '\n')

    (br/'docs'/'API_CONTRACT.md').write_text(dedent('''
    # API Contract

    ## MVP endpoints

    - `POST /api/intake` — create inbound item.
    - `GET /api/items` — list work items.
    - `GET /api/items/{id}` — item detail.
    - `POST /api/items/{id}/classify` — run/refresh AI classification.
    - `POST /api/items/{id}/review` — human approval/rejection/edit decision.
    - `GET /api/metrics` — operational metrics.
    - `GET /api/audit` — audit events.

    ## Security notes

    All endpoints except public intake require authentication. Public intake requires rate limits, validation and abuse detection.
    ''').strip() + '\n')

    (br/'docs'/'ADMIN_OPERATIONS.md').write_text('# Admin Operations\n\n' + '\n'.join('- ' + x for x in b['admin_views']) + '\n')
    (br/'frontend'/'README.md').write_text(f"# Frontend — {b['name']}\n\nLanding/client app scaffold.\n\n## Views\n\n" + '\n'.join('- ' + x for x in b['frontend_views']) + '\n')
    (br/'frontend'/'VIEWS.md').write_text('# Frontend Views\n\n' + '\n'.join('- ' + x for x in b['frontend_views']) + '\n')
    (br/'backend'/'README.md').write_text(f"# Backend — {b['name']}\n\nAPI/services scaffold.\n\n## Motor\n\n" + '\n'.join('- ' + x for x in b['engine']) + '\n')
    (br/'backend'/'MOTOR.md').write_text('# Backend Motor\n\n' + '\n'.join('- ' + x for x in b['engine']) + '\n')
    (br/'admin'/'README.md').write_text(f"# Admin Panel — {b['name']}\n\nControl panel scaffold.\n\n## Views\n\n" + '\n'.join('- ' + x for x in b['admin_views']) + '\n')
    (br/'admin'/'VIEWS.md').write_text('# Admin Panel Views\n\n' + '\n'.join('- ' + x for x in b['admin_views']) + '\n')
    (br/'public-content'/'en'/'POST_IDEAS.md').write_text(dedent(f'''
    # EN Build-in-Public Ideas — {b['name']}

    1. I’m exploring a workflow for {b['buyer']}.
    2. The pain: {b['problem']}
    3. The first MVP is not “AI magic.” It is structured intake, human review and measurable operational improvement.
    4. Positioning line: {b['headline']}
    ''').strip() + '\n')
    (br/'public-content'/'es'/'POST_IDEAS.md').write_text(dedent(f'''
    # ES Adaptación — {b['name']}

    1. Estoy explorando un workflow para: {b['buyer']}.
    2. El dolor: {b['problem']}
    3. El primer MVP no es “magia AI”. Es captura estructurada, revisión humana y mejora operativa medible.
    4. Línea de posicionamiento: {b['es']}
    ''').strip() + '\n')

# Update index and root README preserving all business directories.
all_dirs = sorted([p for p in root.iterdir() if p.is_dir()])
(root / 'INDEX.md').write_text(dedent('''
# Business Index

## Current target

Have 10 internally complete business folders by around 8pm June 8 / next 16h, with documentation, frontend views, backend motor, admin panel views, internal AI system and cybersecurity layer.

## Businesses

''').lstrip() + '\n'.join([f"- [{p.name}]({p.name}/README.md)" for p in all_dirs]) + '\n')

(root / 'README.md').write_text(dedent('''
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
    LANDING_COPY.md
    OUTREACH.md
    DATA_MODEL.md
    API_CONTRACT.md
    ADMIN_OPERATIONS.md
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

## Total actual

10 negocios internos en preparación.
''').strip() + '\n')

print('added', len(new_businesses), 'businesses')
print('total', len(all_dirs))
for p in all_dirs:
    print(p.name)
