from pathlib import Path
from textwrap import dedent

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')
root.mkdir(parents=True, exist_ok=True)

businesses = [
    {
        'slug': 'hvac-missed-call-recovery',
        'name': 'HVAC Missed-Call Recovery',
        'score': '75/90',
        'buyer': 'Owner/operator or operations manager at 3-15 technician HVAC companies in US/Canada/UK/Australia.',
        'user': 'Dispatcher, office admin, on-call technician, owner.',
        'problem': 'Urgent HVAC customers call after hours or during service peaks. If the call goes to voicemail, they often call the next contractor.',
        'offer': 'Done-for-you AI missed-call recovery and after-hours triage: call/SMS intake, emergency qualification, routing rules, job summaries and ROI tracking.',
        'headline': 'Stop losing emergency HVAC jobs to voicemail.',
        'es': 'Deja de perder trabajos urgentes de HVAC por llamadas no contestadas.',
        'palette': ['#0B1F33 deep navy', '#FF6B35 emergency orange', '#2F80ED cool blue', '#F7FAFC clean background', '#111827 text'],
    },
    {
        'slug': 'property-maintenance-triage',
        'name': 'Property Maintenance Triage',
        'score': '71/90',
        'buyer': 'Small property managers, landlords with 20-300 doors, small multifamily operators.',
        'user': 'Tenant, property manager, maintenance coordinator, approved vendors.',
        'problem': 'Tenants send vague maintenance texts at all hours; managers waste time classifying urgency, requesting photos, routing vendors and documenting response.',
        'offer': 'AI maintenance intake and triage inbox: tenant form/SMS, photo prompts, urgency scoring, vendor message drafts and audit logs.',
        'headline': 'Turn vague tenant maintenance texts into clean work orders.',
        'es': 'Convierte mensajes vagos de mantenimiento en órdenes de trabajo claras.',
        'palette': ['#12372A property green', '#436850 operational green', '#FBFADA warm background', '#ADBC9F muted accent', '#111827 text'],
    },
    {
        'slug': 'construction-bid-inbox',
        'name': 'Construction Bid Inbox Copilot',
        'score': '69/90',
        'buyer': 'Subcontractor owner, estimator, preconstruction manager, small GC.',
        'user': 'Estimator handling bid invites, addenda, RFIs, quote leveling and proposal emails.',
        'problem': 'Estimators drown in bid invites, addenda, deadlines and proposal revisions. Missing one addendum can erase profit.',
        'offer': 'AI bid inbox that extracts due dates, RFI deadlines, addenda, contacts, scope notes, and next actions from forwarded bid emails.',
        'headline': 'Your bid inbox should not be your preconstruction system.',
        'es': 'Tu inbox de licitaciones no debería ser tu sistema de preconstrucción.',
        'palette': ['#111827 charcoal', '#F59E0B construction amber', '#2563EB blueprint blue', '#F3F4F6 light surface', '#DC2626 risk red'],
    },
    {
        'slug': 'dental-insurance-checklist',
        'name': 'Dental Insurance Checklist Assistant',
        'score': '62/90',
        'buyer': 'Dental practice owner, office manager, small DSO operations lead.',
        'user': 'Front desk, treatment coordinator, insurance coordinator.',
        'problem': 'Dental teams manually verify eligibility/benefits and deal with denied claims, patient confusion and same-day surprises.',
        'offer': 'Pre-visit dental benefits checklist workflow: patient intake, verification status, payer checklist, benefit-summary templates and PMS-ready notes.',
        'headline': 'Make dental insurance verification less painful before the patient arrives.',
        'es': 'Haz menos dolorosa la verificación de seguro dental antes de que llegue el paciente.',
        'palette': ['#0F766E teal', '#14B8A6 dental mint', '#F0FDFA clean background', '#134E4A dark text', '#F97316 warning accent'],
    },
]

(root / 'README.md').write_text(dedent('''
# Business Incubation Output

Carpeta interna para que AION vaya preparando negocios completos dentro del repo actual antes de que Andre los suba a GitHub como repos privados o separados.

## Reglas

- No deployar.
- No tocar Nexbody.
- No usar datos reales de clientes.
- Public assets EN-first; adaptación ES después.
- Cada negocio debe tener documentación, frontend, backend y panel de control/admin.

## Estructura

```text
output/businesses/<business-slug>/
  README.md
  docs/
  frontend/
  backend/
  admin/
  public-content/
```

## Negocios iniciales

1. `hvac-missed-call-recovery` — primera prioridad.
2. `property-maintenance-triage` — segunda prioridad.
3. `construction-bid-inbox` — tercera prioridad.
4. `dental-insurance-checklist` — en observación por compliance.
''').strip() + '\n')

(root / 'INDEX.md').write_text('# Business Index\n\n' + '\n'.join([f"- [{b['name']}]({b['slug']}/README.md) — {b['score']}" for b in businesses]) + '\n')

for b in businesses:
    br = root / b['slug']
    for sub in ['docs', 'frontend/src', 'backend/src', 'admin/src', 'public-content/en', 'public-content/es']:
        (br / sub).mkdir(parents=True, exist_ok=True)
    (br / 'README.md').write_text(dedent(f'''
    # {b['name']}

    **Score:** {b['score']}

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

    - `docs/` — business, audience, brand, validation and technical specs.
    - `frontend/` — landing/client app scaffold.
    - `backend/` — API/services scaffold.
    - `admin/` — control panel scaffold.
    - `public-content/` — build-in-public content EN/ES.

    ## Current status

    Internal scaffold only. No deploy. No GitHub publication yet.
    ''').strip() + '\n')
    (br / 'docs' / 'BUSINESS_PLAN.md').write_text(dedent(f'''
    # Business Plan — {b['name']}

    ## Goal

    Build a small, monetizable AI workflow product/service for an English-speaking market with clear willingness to pay.

    ## Target buyer

    {b['buyer']}

    ## Pain

    {b['problem']}

    ## Offer

    {b['offer']}

    ## Revenue model hypothesis

    - Setup fee for done-for-you configuration.
    - Monthly subscription/support.
    - Optional paid pilot before full productization.

    ## Validation gate

    Do not overbuild until there is at least one of:

    - 2 discovery calls.
    - 1 paid pilot/LOI.
    - 5+ meaningful replies from target buyers.
    - 1 operator willing to test fake/manual MVP flow.
    ''').strip() + '\n')
    (br / 'docs' / 'TARGET_AUDIENCE.md').write_text(dedent(f'''
    # Target Audience — {b['name']}

    ## Buyer

    {b['buyer']}

    ## User

    {b['user']}

    ## Why English-speaking market first

    Higher SaaS/service buying culture, stronger USD pricing potential, and better channels for B2B outreach/content.

    ## Spanish angle

    Spanish adaptation is useful for bilingual operators, Hispanic-owned businesses, or end users who communicate better in Spanish.
    ''').strip() + '\n')
    (br / 'docs' / 'BRAND_KIT.md').write_text(dedent(f'''
    # Brand Kit — {b['name']}

    ## Positioning line

    **EN:** {b['headline']}

    **ES:** {b['es']}

    ## Tone

    Operational, practical, ROI-driven, clear, not hypey.

    ## Palette

    {chr(10).join('- ' + color for color in b['palette'])}
    ''').strip() + '\n')
    (br / 'docs' / 'TECH_SPEC.md').write_text(dedent(f'''
    # Technical Spec — {b['name']}

    ## Repo pattern

    This folder simulates 3 future repos:

    - `backend/` — API, data model, automations, integrations.
    - `frontend/` — landing/client experience.
    - `admin/` — internal control panel.

    ## Backend initial responsibilities

    - Entities and persistence.
    - Intake endpoints.
    - AI classification/summarization helper.
    - Notification/routing placeholders.
    - Audit logs.

    ## Frontend initial responsibilities

    - English-first landing page.
    - ROI/value calculator where relevant.
    - Demo flow pages.
    - Waitlist/audit request CTA.

    ## Admin initial responsibilities

    - Dashboard list view.
    - Detail pages.
    - Configuration/rules UI.
    - Status and manual review controls.
    ''').strip() + '\n')
    (br / 'docs' / 'VALIDATION_PLAN.md').write_text(dedent(f'''
    # Validation Plan — {b['name']}

    ## Before building deeply

    1. Prepare English landing copy.
    2. Prepare cold outreach script.
    3. Create fake demo data.
    4. Identify 20 target prospects.
    5. Ask for discovery calls, not immediate SaaS signup.

    ## Success signal

    A target buyer says: “I have this problem, I would try this, and I understand why it costs money.”
    ''').strip() + '\n')
    (br / 'frontend' / 'README.md').write_text(dedent(f'''
    # Frontend — {b['name']}

    Landing/client app scaffold.

    ## First screens

    - Landing hero: `{b['headline']}`
    - Problem section.
    - Workflow demo section.
    - Pricing/ROI hypothesis.
    - CTA: free audit / waitlist / discovery call.
    ''').strip() + '\n')
    (br / 'backend' / 'README.md').write_text(dedent(f'''
    # Backend — {b['name']}

    API/services scaffold.

    ## First modules

    - Intake
    - Classification
    - Summary generation
    - Routing/notifications
    - Audit log
    ''').strip() + '\n')
    (br / 'admin' / 'README.md').write_text(dedent(f'''
    # Admin Panel — {b['name']}

    Control panel scaffold.

    ## First modules

    - Dashboard
    - Records/leads/work items
    - Rules/settings
    - Manual review
    - Metrics
    ''').strip() + '\n')
    (br / 'public-content' / 'en' / 'POST_IDEAS.md').write_text(dedent(f'''
    # EN Build-in-Public Ideas — {b['name']}

    1. Building a workflow for operators who still run critical work through voicemail, SMS, inboxes and spreadsheets.
    2. The problem: {b['problem']}
    3. The first MVP is not full automation. It is cleaner intake, routing and decision support.
    ''').strip() + '\n')
    (br / 'public-content' / 'es' / 'POST_IDEAS.md').write_text(dedent(f'''
    # ES Adaptación — {b['name']}

    1. Construyendo un flujo AI para operadores que todavía gestionan trabajo crítico por voicemail, SMS, inbox y spreadsheets.
    2. El problema: {b['problem']}
    3. El primer MVP no es automatización total. Es mejor captura, clasificación y soporte de decisión.
    ''').strip() + '\n')

print(root)
for b in businesses:
    print(root / b['slug'])
