from pathlib import Path
from textwrap import dedent

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')

for br in sorted([p for p in root.iterdir() if p.is_dir()]):
    name = br.name.replace('-', ' ').title()
    readme = (br / 'README.md').read_text() if (br / 'README.md').exists() else f'# {name}\n'
    headline = None
    for marker in ['## English-first positioning', '## Positioning line']:
        if marker in readme:
            after = readme.split(marker, 1)[1].strip().splitlines()
            headline = next((line.strip('* ') for line in after if line.strip() and not line.startswith('##')), None)
            break
    if not headline:
        headline = f'Operational AI workflow for {name}.'

    docs = br / 'docs'
    docs.mkdir(exist_ok=True)
    frontend_views = (br / 'frontend' / 'VIEWS.md').read_text() if (br / 'frontend' / 'VIEWS.md').exists() else '# Frontend Views\n\n- Landing page\n- Demo page\n- Request audit page\n'
    backend_motor = (br / 'backend' / 'MOTOR.md').read_text() if (br / 'backend' / 'MOTOR.md').exists() else '# Backend Motor\n\n- Intake\n- Classification\n- Review\n- Metrics\n'
    admin_views = (br / 'admin' / 'VIEWS.md').read_text() if (br / 'admin' / 'VIEWS.md').exists() else '# Admin Panel Views\n\n- Dashboard\n- Detail view\n- Settings\n- Audit log\n'

    files = {
        'LANDING_COPY.md': dedent(f'''
        # Landing Copy — {name}

        ## Hero

        {headline}

        ## Subheadline

        A focused AI-assisted workflow for operators who need structured intake, faster review, cleaner follow-up and measurable business outcomes.

        ## Primary CTA

        Get a free workflow audit.

        ## Secondary CTA

        See the demo flow.

        ## Sections

        1. Pain/problem.
        2. What the workflow does.
        3. Before/after operational example.
        4. Security and human review.
        5. Pilot offer.
        6. FAQ.

        ## Spanish adaptation

        Un workflow AI enfocado para operadores que necesitan mejor captura, revisión rápida, follow-up claro y resultados medibles.
        ''').strip() + '\n',
        'OUTREACH.md': dedent(f'''
        # Outreach — {name}

        ## Cold email v0

        Subject: quick workflow question

        Hi {{first_name}},

        I’m researching a small AI-assisted workflow around this problem:

        > {headline}

        The first version is not a big platform. It is a focused workflow with structured intake, human review, audit logs and measurable ROI.

        Would a 15-minute sanity-check call next week be unreasonable?

        — Andre

        ## Follow-up

        Totally understand if now is not the right time. If this is not painful in your operation, that is useful to know too.
        ''').strip() + '\n',
        'DATA_MODEL.md': dedent('''
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
        - IntegrationCredentialReference — reference only; no raw secrets in app logs/docs.

        ## Notes

        Keep the MVP relational and auditable. Prefer simple Postgres/SQLite-compatible models first, then integrations later.
        ''').strip() + '\n',
        'API_CONTRACT.md': dedent('''
        # API Contract

        ## MVP endpoints

        - `POST /api/intake` — create inbound item.
        - `GET /api/items` — list work items.
        - `GET /api/items/{id}` — item detail.
        - `POST /api/items/{id}/classify` — run/refresh AI classification.
        - `POST /api/items/{id}/review` — human approval/rejection/edit decision.
        - `PATCH /api/items/{id}/status` — update workflow state.
        - `GET /api/metrics` — operational metrics.
        - `GET /api/audit` — audit events.

        ## Security notes

        Public intake must be rate-limited and validated. All operational/admin endpoints require authentication, authorization and audit logs.
        ''').strip() + '\n',
        'ADMIN_OPERATIONS.md': dedent(f'''
        # Admin Operations — {name}

        ## Admin views source

        {admin_views}

        ## Daily workflow

        1. Review new inbound items.
        2. Check AI classifications and low-confidence flags.
        3. Approve, edit or reject suggested actions/messages.
        4. Assign owner/status.
        5. Review metrics and unresolved exceptions.

        ## Weekly workflow

        1. Review conversion/recovery metrics.
        2. Audit rule/template performance.
        3. Identify bottlenecks.
        4. Export summary for owner/founder review.
        ''').strip() + '\n',
        'FRONTEND_VIEW_MAP.md': dedent(f'''
        # Frontend View Map — {name}

        {frontend_views}
        ''').strip() + '\n',
        'BACKEND_MOTOR_MAP.md': dedent(f'''
        # Backend Motor Map — {name}

        {backend_motor}
        ''').strip() + '\n',
    }
    for filename, content in files.items():
        target = docs / filename
        if not target.exists():
            target.write_text(content)

print('ensured extended docs for', len([p for p in root.iterdir() if p.is_dir()]), 'businesses')
