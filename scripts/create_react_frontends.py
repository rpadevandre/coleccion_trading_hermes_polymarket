from pathlib import Path
from textwrap import dedent
import re

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')

businesses = {
    'hvac-missed-call-recovery': {
        'name': 'HVAC Missed-Call Recovery',
        'headline': 'Recover revenue from missed HVAC calls before competitors win the job.',
        'subheadline': 'AI-assisted intake, urgency triage and dispatch notifications for small HVAC operators.',
        'accent': '#2563eb',
        'metric': '$8k-$40k/mo potential revenue leakage surfaced',
        'views': [
            ('Landing', 'Public validation landing page for HVAC owners.'),
            ('ROICalculator', 'Interactive calculator for missed-call revenue leakage.'),
            ('DemoCallFlow', 'Visual call-to-dispatch demo flow.'),
            ('FreeAuditForm', 'Lead capture form for operational audit.'),
            ('PilotSignup', 'Pilot conversion page for qualified companies.'),
        ],
    },
    'property-maintenance-triage': {
        'name': 'Property Maintenance Triage',
        'headline': 'Turn tenant maintenance chaos into prioritized work orders.',
        'subheadline': 'AI triage for property managers handling requests across texts, email and forms.',
        'accent': '#059669',
        'metric': 'Hours saved per manager per week',
        'views': [
            ('Landing', 'Public validation landing page for property managers.'),
            ('TenantRequestDemo', 'Demo request intake and triage result.'),
            ('ROICalculator', 'Calculator for manager time saved and emergency leakage.'),
            ('PortfolioAuditForm', 'Audit form for unit count and workflow pain.'),
            ('PilotSignup', 'Pilot booking page.'),
        ],
    },
    'construction-bid-inbox': {
        'name': 'Construction Bid Inbox',
        'headline': 'Stop losing bid opportunities inside messy inboxes.',
        'subheadline': 'Extract scope, due dates, fit scores and estimator checklists from bid requests.',
        'accent': '#ea580c',
        'metric': 'More bids reviewed without more admin work',
        'views': [
            ('Landing', 'Public validation page for contractors.'),
            ('BidInboxDemo', 'Demo bid request extraction.'),
            ('PipelineCalculator', 'Calculator for admin hours and bid throughput.'),
            ('TradeFitForm', 'Trade/geography fit intake form.'),
            ('PilotSignup', 'Pilot signup page.'),
        ],
    },
    'dental-insurance-checklist': {
        'name': 'Dental Insurance Checklist',
        'headline': 'Give dental teams a safer insurance verification checklist.',
        'subheadline': 'Procedure-specific verification steps with human review and PHI-conscious workflows.',
        'accent': '#0891b2',
        'metric': 'Reduce verification rework and missed fields',
        'views': [
            ('Landing', 'Public validation page for dental offices.'),
            ('ChecklistDemo', 'Demo procedure-specific checklist.'),
            ('ReworkCalculator', 'Calculator for verification admin rework.'),
            ('OfficeAuditForm', 'Office workflow audit form.'),
            ('PilotSignup', 'Controlled pilot signup page.'),
        ],
    },
    'msp-security-reporting': {
        'name': 'MSP Security Reporting Copilot',
        'headline': 'Turn security work into client-ready reports MSPs can actually sell.',
        'subheadline': 'Transform ticket/security evidence into executive summaries and monthly proof-of-value reports.',
        'accent': '#7c3aed',
        'metric': 'Monthly report production time cut dramatically',
        'views': [
            ('Landing', 'Public validation page for MSPs.'),
            ('ReportBeforeAfter', 'Raw technical noise vs executive report.'),
            ('ClientProofDemo', 'Demo client report approval flow.'),
            ('StackAuditForm', 'Tool stack and reporting pain intake.'),
            ('PilotSignup', 'Pilot signup on anonymized report sample.'),
        ],
    },
    'med-spa-lead-recovery': {
        'name': 'Med Spa Lead Recovery',
        'headline': 'Recover med-spa leads before they book somewhere else.',
        'subheadline': 'AI-assisted lead capture and human-approved consult follow-up for aesthetic clinics.',
        'accent': '#db2777',
        'metric': 'Booked consults recovered from slow replies',
        'views': [
            ('Landing', 'Public validation page for med spas.'),
            ('LeadLeakCalculator', 'Calculator for lost consult value.'),
            ('InstagramDMFlow', 'Demo DM/form/call to consult flow.'),
            ('FreeLeadAuditForm', 'Lead workflow audit form.'),
            ('PilotSignup', 'Pilot conversion page.'),
        ],
    },
    'law-firm-intake-triage': {
        'name': 'Law Firm Intake Triage',
        'headline': 'Convert messy legal inquiries into attorney-ready intake summaries.',
        'subheadline': 'Practice-area triage, missing-fact checklists and human review without giving legal advice.',
        'accent': '#334155',
        'metric': 'Cleaner intake before attorney review',
        'views': [
            ('Landing', 'Public validation page for law firms.'),
            ('PracticeAreaDemo', 'Demo inquiry classification.'),
            ('IntakeQualityCalculator', 'Calculator for staff/attorney time saved.'),
            ('FirmAuditForm', 'Firm intake workflow audit form.'),
            ('PilotSignup', 'Pilot signup page.'),
        ],
    },
    'chiropractic-reactivation-engine': {
        'name': 'Chiropractic Reactivation Engine',
        'headline': 'Reactivate inactive patients with gentle, approved campaigns.',
        'subheadline': 'Segment inactive patient lists, draft messages and track recovered appointments.',
        'accent': '#16a34a',
        'metric': 'Recovered appointments from existing patient lists',
        'views': [
            ('Landing', 'Public validation page for chiropractic clinics.'),
            ('RecoveryCalculator', 'Calculator for recovered appointments.'),
            ('CampaignPreview', 'Demo segment and message preview.'),
            ('InactiveListAuditForm', 'Inactive list audit form.'),
            ('PilotSignup', 'Pilot signup page.'),
        ],
    },
    'restaurant-catering-followup': {
        'name': 'Restaurant Catering Follow-Up Copilot',
        'headline': 'Stop catering inquiries from dying in the inbox.',
        'subheadline': 'Capture event details, reminders and quote checklists for restaurants selling catering.',
        'accent': '#dc2626',
        'metric': 'Catering revenue recovered from faster follow-up',
        'views': [
            ('Landing', 'Public validation page for restaurants.'),
            ('EventInquiryDemo', 'Demo inquiry parsing.'),
            ('CateringRevenueCalculator', 'Calculator for lost catering value.'),
            ('InboxAuditForm', 'Inbox workflow audit form.'),
            ('PilotSignup', 'Pilot signup page.'),
        ],
    },
    'b2b-podcast-repurposing-system': {
        'name': 'B2B Podcast Repurposing System',
        'headline': 'Turn one B2B conversation into a week of founder-led content.',
        'subheadline': 'Extract insights, draft channel-native posts and queue content for approval.',
        'accent': '#4f46e5',
        'metric': 'One source conversation → multi-channel content queue',
        'views': [
            ('Landing', 'Public validation page for founders/content teams.'),
            ('BeforeAfterDemo', 'Demo transcript to content transformation.'),
            ('TranscriptUploadDemo', 'Transcript paste/upload demo.'),
            ('ContentCalendarPreview', 'Calendar preview page.'),
            ('EpisodeAuditForm', 'Episode/source audit form.'),
        ],
    },
}

def slugify_view(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

def component_code(b, view_name, description):
    route = slugify_view(view_name)
    is_calc = 'Calculator' in view_name
    is_form = 'Form' in view_name or 'Signup' in view_name or 'Audit' in view_name
    is_demo = 'Demo' in view_name or 'Flow' in view_name or 'Preview' in view_name
    calc_block = """
      <section className=\"card interactive-card\">
        <h2>Quick estimate</h2>
        <div className=\"calc-grid\">
          <label>Weekly volume<input type=\"number\" defaultValue={25} /></label>
          <label>Average value<input type=\"number\" defaultValue={750} /></label>
          <label>Recovery rate<input type=\"number\" defaultValue={20} /></label>
        </div>
        <p className=\"result\">Use this in the first MVP to calculate estimated recovered value before asking for a demo.</p>
      </section>
""" if is_calc else """
      <section className=\"card\">
        <h2>Primary outcome</h2>
        <p>{viewMeta.primaryOutcome}</p>
      </section>
"""
    form_block = """
      <section className=\"card\">
        <h2>Qualification form</h2>
        <form className=\"stack\">
          <input placeholder=\"Work email\" />
          <input placeholder=\"Company / practice name\" />
          <input placeholder=\"Current monthly volume\" />
          <textarea placeholder=\"What is currently breaking in this workflow?\" />
          <button type=\"button\">Request pilot review</button>
        </form>
      </section>
""" if is_form else """
      <section className=\"card\">
        <h2>CTA</h2>
        <button type=\"button\">Book a workflow audit</button>
      </section>
"""
    demo_block = """
      <section className=\"card\">
        <h2>Demo sequence</h2>
        <ol>
          <li>Capture source event or message.</li>
          <li>AI extracts structured fields with confidence.</li>
          <li>Human reviews suggested action.</li>
          <li>Admin panel tracks outcome and audit trail.</li>
        </ol>
      </section>
""" if is_demo else """
      <section className=\"card\">
        <h2>How it works</h2>
        <ol>
          <li>Import or capture the workflow item.</li>
          <li>Classify, summarize and flag missing information.</li>
          <li>Route to the right human with an audit trail.</li>
        </ol>
      </section>
"""
    return dedent(f"""
    import React from 'react';
    import {{ businessMeta, frontendViews }} from '../businessMeta';
    import '../styles.css';

    const viewMeta = frontendViews.find((view) => view.name === '{view_name}') ?? {{
      name: '{view_name}',
      path: '/{route}',
      description: '{description}',
      primaryOutcome: 'Validate buyer demand and move qualified users into a pilot.'
    }};

    export default function {view_name}() {{
      return (
        <main className=\"business-page\" style={{{{ '--accent': businessMeta.accent }} as React.CSSProperties}}>
          <section className=\"hero\">
            <p className=\"eyebrow\">{{businessMeta.name}}</p>
            <h1>{{viewMeta.name}}</h1>
            <p className=\"lede\">{{viewMeta.description}}</p>
            <p className=\"metric\">{{businessMeta.metric}}</p>
          </section>
    {demo_block.rstrip()}
    {calc_block.rstrip()}
    {form_block.rstrip()}
          <section className=\"guardrail\">
            <strong>Human-in-loop:</strong> AI suggestions stay reviewable, auditable and reversible before any customer-facing action.
          </section>
        </main>
      );
    }}
    """).strip() + "\n"

def app_code(b):
    imports = [f"import {name} from './views/{name}';" for name, _ in b['views']]
    route_entries = [f"  '{slugify_view(name)}': {name}," for name, _ in b['views']]
    nav_buttons = [f"          <button onClick={{() => setRoute('{slugify_view(name)}')}} className={{route === '{slugify_view(name)}' ? 'active' : ''}}>{name}</button>" for name, _ in b['views']]
    default = slugify_view(b['views'][0][0])
    return dedent(f"""
    import React, {{ useMemo, useState }} from 'react';
    {chr(10).join(imports)}
    import {{ businessMeta }} from './businessMeta';
    import './styles.css';

    const routes = {{
    {chr(10).join(route_entries)}
    }};

    export default function App() {{
      const [route, setRoute] = useState<keyof typeof routes>('{default}');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className=\"app-shell\">
          <nav className=\"top-nav\">
            <strong>{{businessMeta.name}}</strong>
    {chr(10).join(nav_buttons)}
          </nav>
          <ActiveView />
        </div>
      );
    }}
    """).strip() + "\n"

def meta_code(b):
    view_lines = []
    for name, desc in b['views']:
        path = '/' + slugify_view(name)
        outcome = 'Convert this page into validated pilot interest with measurable buyer signal.'
        view_lines.append(f"  {{ name: '{name}', path: '{path}', description: '{desc}', primaryOutcome: '{outcome}' }},")
    return dedent(f"""
    export const businessMeta = {{
      name: '{b['name']}',
      headline: '{b['headline']}',
      subheadline: '{b['subheadline']}',
      accent: '{b['accent']}',
      metric: '{b['metric']}',
    }} as const;

    export const frontendViews = [
    {chr(10).join(view_lines)}
    ] as const;
    """).strip() + "\n"

styles = """
:root { font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #0f172a; background: #f8fafc; }
* { box-sizing: border-box; }
body { margin: 0; }
.app-shell { min-height: 100vh; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); }
.top-nav { position: sticky; top: 0; z-index: 5; display: flex; gap: .5rem; align-items: center; flex-wrap: wrap; padding: .85rem 1rem; border-bottom: 1px solid #e2e8f0; background: rgba(255,255,255,.92); backdrop-filter: blur(12px); }
.top-nav strong { margin-right: auto; }
.top-nav button { border: 1px solid #cbd5e1; background: #fff; border-radius: 999px; padding: .45rem .75rem; cursor: pointer; }
.top-nav button.active { color: #fff; background: var(--accent, #2563eb); border-color: var(--accent, #2563eb); }
.business-page { --accent: #2563eb; width: min(1080px, calc(100% - 2rem)); margin: 0 auto; padding: 2rem 0 4rem; }
.hero { padding: 2rem; border-radius: 28px; background: radial-gradient(circle at top right, color-mix(in srgb, var(--accent) 22%, white), white 44%); border: 1px solid #e2e8f0; box-shadow: 0 18px 50px rgba(15, 23, 42, .08); }
.eyebrow { margin: 0 0 .5rem; color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: .12em; font-size: .75rem; }
h1 { margin: 0; font-size: clamp(2rem, 5vw, 4rem); line-height: 1; }
.lede { max-width: 760px; color: #475569; font-size: 1.15rem; line-height: 1.6; }
.metric { display: inline-flex; padding: .55rem .85rem; border-radius: 999px; background: color-mix(in srgb, var(--accent) 12%, white); color: #0f172a; font-weight: 700; }
.card { margin-top: 1rem; padding: 1.25rem; border: 1px solid #e2e8f0; background: #fff; border-radius: 20px; box-shadow: 0 10px 30px rgba(15, 23, 42, .04); }
.card h2 { margin-top: 0; }
.stack { display: grid; gap: .75rem; }
input, textarea { width: 100%; border: 1px solid #cbd5e1; border-radius: 14px; padding: .8rem 1rem; font: inherit; }
textarea { min-height: 110px; }
button { border: 0; border-radius: 14px; padding: .8rem 1rem; background: var(--accent, #2563eb); color: #fff; font-weight: 700; }
.calc-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .75rem; }
.calc-grid label { display: grid; gap: .35rem; font-weight: 700; color: #334155; }
.result, .guardrail { color: #475569; }
.guardrail { margin-top: 1rem; padding: 1rem; border-left: 4px solid var(--accent); background: #fff; border-radius: 14px; }
@media (max-width: 720px) { .calc-grid { grid-template-columns: 1fr; } .top-nav { align-items: flex-start; } }
""".strip() + "\n"

package_json = """{
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "vite build",
    "preview": "vite preview --host 0.0.0.0"
  },
  "dependencies": {
    "@vitejs/plugin-react": "latest",
    "vite": "latest",
    "typescript": "latest",
    "react": "latest",
    "react-dom": "latest"
  },
  "devDependencies": {}
}
"""

tsconfig = """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ES2020"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "references": []
}
"""

vite_config = """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});
"""

index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Business Frontend Prototype</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""

main_tsx = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""

for slug, b in businesses.items():
    base = root / slug / 'frontend'
    src = base / 'src'
    views = src / 'views'
    views.mkdir(parents=True, exist_ok=True)
    (src / 'businessMeta.ts').write_text(meta_code(b))
    (src / 'App.tsx').write_text(app_code(b))
    (src / 'main.tsx').write_text(main_tsx)
    (src / 'styles.css').write_text(styles)
    (base / 'package.json').write_text(package_json)
    (base / 'tsconfig.json').write_text(tsconfig)
    (base / 'vite.config.ts').write_text(vite_config)
    (base / 'index.html').write_text(index_html)
    for view_name, desc in b['views']:
        (views / f'{view_name}.tsx').write_text(component_code(b, view_name, desc))
    (base / 'REACT_IMPLEMENTATION.md').write_text(dedent(f"""
    # React Implementation — {b['name']}

    This frontend is a Vite + React + TypeScript prototype scaffold for internal incubation.

    ## Views implemented

    {chr(10).join('- `src/views/' + name + '.tsx` — ' + desc for name, desc in b['views'])}

    ## Local run after repo split

    ```bash
    npm install
    npm run dev
    ```

    ## Current limitation

    This is intentionally local/prototype code under `output/businesses`. It is not deployed and has no production API connection yet.
    """).strip() + "\n")

print(f'created React frontend files for {len(businesses)} businesses')
