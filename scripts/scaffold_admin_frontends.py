#!/usr/bin/env python3
"""Generate lightweight admin panel frontends for incubated businesses.

The admin layer is intentionally dependency-free for now: plain HTML/CSS/JS that
can talk to the FastAPI scaffold endpoints. This makes every business inspectable
from GitHub and runnable locally without a frontend build step.
"""
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parents[1] / "output" / "businesses"

BUSINESSES = {
    "hvac-missed-call-recovery": {
        "title": "HVAC Missed-Call Recovery",
        "operator": "dispatch/revenue ops manager",
        "queue": "Dispatch Recovery Queue",
        "primary_metric": "Recovered revenue pipeline",
        "secondary_metric": "Urgent missed calls",
        "accent": "#f97316",
        "views": ["Recovery Queue", "Urgency Review", "Revenue Estimate", "Dispatch Routing", "Audit Log"],
        "sample": "Emergency AC repair request after-hours. Customer left voicemail and needs callback today.",
        "signals": {"service_type": "AC repair", "after_hours": True, "zip_code": "33101", "call_time": "18:42"},
    },
    "property-maintenance-triage": {
        "title": "Property Maintenance Triage",
        "operator": "property maintenance coordinator",
        "queue": "Maintenance Triage Queue",
        "primary_metric": "Open tenant requests",
        "secondary_metric": "SLA risk tickets",
        "accent": "#22c55e",
        "views": ["Tenant Requests", "Urgency Triage", "Vendor Routing", "SLA Watch", "Tenant Summary"],
        "sample": "Tenant reports water leaking under sink and possible mold smell in unit.",
        "signals": {"issue_category": "plumbing", "photos_available": False, "after_hours": False, "unit_id": "A-204"},
    },
    "construction-bid-inbox": {
        "title": "Construction Bid Inbox",
        "operator": "estimating manager",
        "queue": "Bid Review Queue",
        "primary_metric": "Qualified bid opportunities",
        "secondary_metric": "Deadlines this week",
        "accent": "#eab308",
        "views": ["Bid Inbox", "Scope Extraction", "Trade Fit", "Checklist", "Pipeline"],
        "sample": "Invitation to bid commercial tenant improvement project. Electrical scope due Friday.",
        "signals": {"trade": "electrical", "deadline": "Friday", "project_location": "Austin TX", "estimated_value": 85000},
    },
    "dental-insurance-checklist": {
        "title": "Dental Insurance Checklist",
        "operator": "dental treatment coordinator",
        "queue": "Verification Review Queue",
        "primary_metric": "Verifications pending",
        "secondary_metric": "Missing policy fields",
        "accent": "#06b6d4",
        "views": ["Verification Cases", "Checklist Builder", "Policy Summary", "Compliance Guard", "Audit Trail"],
        "sample": "Patient scheduled for crown procedure; coverage details and waiting period unclear.",
        "signals": {"payer": "Delta Dental", "procedure_type": "crown", "appointment_date": "next_week", "missing_fields": ["waiting_period"]},
    },
    "msp-security-reporting": {
        "title": "MSP Security Reporting",
        "operator": "MSP account/security lead",
        "queue": "Client Reporting Queue",
        "primary_metric": "Reports awaiting approval",
        "secondary_metric": "High severity findings",
        "accent": "#8b5cf6",
        "views": ["Evidence Inbox", "Risk Narrative", "Client Report", "Approval Queue", "Audit Trail"],
        "sample": "Endpoint alerts show repeated failed login attempts and missing MFA on admin account.",
        "signals": {"client_name": "Acme Dental", "finding_type": "identity", "severity": "high", "recommended_action": "enable MFA"},
    },
    "med-spa-lead-recovery": {
        "title": "Med Spa Lead Recovery",
        "operator": "med spa owner/front desk manager",
        "queue": "Consult Recovery Queue",
        "primary_metric": "Unbooked consult value",
        "secondary_metric": "Hot treatment leads",
        "accent": "#ec4899",
        "views": ["Lead Inbox", "Treatment Intent", "Follow-up Drafts", "Compliance Guard", "Booked Revenue"],
        "sample": "Instagram lead asked about Botox pricing and never booked a consultation.",
        "signals": {"lead_source": "Instagram DM", "treatment_interest": "Botox", "booking_status": "not_booked", "last_contacted_at": "3_days_ago"},
    },
    "law-firm-intake-triage": {
        "title": "Law Firm Intake Triage",
        "operator": "law firm intake coordinator",
        "queue": "Attorney Review Queue",
        "primary_metric": "Qualified intake cases",
        "secondary_metric": "Urgent deadlines",
        "accent": "#0f766e",
        "views": ["Inquiry Inbox", "Practice Area", "Conflict Checklist", "Attorney Summary", "Audit Log"],
        "sample": "Potential client asks about employment termination and upcoming filing deadline.",
        "signals": {"practice_area": "employment", "deadline": "soon", "jurisdiction": "Florida", "opposing_party": "former employer"},
    },
    "chiropractic-reactivation-engine": {
        "title": "Chiropractic Reactivation Engine",
        "operator": "clinic growth/front desk manager",
        "queue": "Reactivation Review Queue",
        "primary_metric": "Patients ready for outreach",
        "secondary_metric": "Recovered appointments",
        "accent": "#84cc16",
        "views": ["Patient Segments", "Message Drafts", "Suppression List", "Campaign Review", "Recovered Appointments"],
        "sample": "Inactive patient has not visited in 8 months and previously completed care plan phase 1.",
        "signals": {"last_visit_date": "8_months_ago", "patient_status": "inactive", "preferred_channel": "SMS", "opt_out_status": False},
    },
    "restaurant-catering-followup": {
        "title": "Restaurant Catering Followup",
        "operator": "catering/event manager",
        "queue": "Catering Follow-up Queue",
        "primary_metric": "Open catering inquiries",
        "secondary_metric": "Event value at risk",
        "accent": "#ef4444",
        "views": ["Inquiry Inbox", "Event Details", "Quote Checklist", "Follow-up Reminders", "Booked Revenue"],
        "sample": "Corporate lunch inquiry for 80 guests next month; quote not sent yet.",
        "signals": {"event_date": "next_month", "guest_count": 80, "budget": "unknown", "event_type": "corporate_lunch"},
    },
    "b2b-podcast-repurposing-system": {
        "title": "B2B Podcast Repurposing System",
        "operator": "founder/content operator",
        "queue": "Content Asset Queue",
        "primary_metric": "Episodes awaiting repurpose",
        "secondary_metric": "Draft assets ready",
        "accent": "#3b82f6",
        "views": ["Episode Inbox", "Insight Extraction", "Channel Drafts", "Voice Score", "Publishing Queue"],
        "sample": "Founder interview about AI operations needs LinkedIn posts and newsletter angle.",
        "signals": {"episode_title": "AI Ops for SMBs", "target_channel": "LinkedIn", "buyer_persona": "SMB founder", "campaign_goal": "demo_calls"},
    },
}


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def html(slug: str, cfg: dict) -> str:
    sample_json = json.dumps({"message": cfg["sample"], "signals": cfg["signals"]}, indent=2)
    views = "".join(f'<button class="view-tab" data-view="{view}">{view}</button>' for view in cfg["views"])
    cards = "".join(f'<article class="view-card"><span>View</span><strong>{view}</strong><p>Operational surface for {cfg["operator"]}.</p></article>' for view in cfg["views"])
    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{cfg['title']} Admin Panel</title>
        <link rel="stylesheet" href="./styles.css" />
      </head>
      <body data-slug="{slug}">
        <div class="shell">
          <aside class="sidebar">
            <p class="eyebrow">AION Admin</p>
            <h1>{cfg['title']}</h1>
            <p class="operator">For {cfg['operator']}.</p>
            <nav>{views}</nav>
            <div class="api-box">
              <label for="apiBase">FastAPI base URL</label>
              <input id="apiBase" value="http://localhost:8000" />
              <small>Backend currently uses in-memory storage; MongoDB is planned but disabled.</small>
            </div>
          </aside>

          <main>
            <section class="hero">
              <div>
                <p class="eyebrow">Internal operator dashboard</p>
                <h2>{cfg['queue']}</h2>
                <p>Admin frontend scaffold connected to the FastAPI contract: health, meta, intake creation, scoring, and queue review.</p>
              </div>
              <button id="checkHealth">Check API</button>
            </section>

            <section class="metrics">
              <article><span>Primary metric</span><strong>{cfg['primary_metric']}</strong><em id="primaryMetric">--</em></article>
              <article><span>Secondary metric</span><strong>{cfg['secondary_metric']}</strong><em id="secondaryMetric">--</em></article>
              <article><span>API status</span><strong id="apiStatus">Not checked</strong><em>Local FastAPI</em></article>
            </section>

            <section class="grid">
              <article class="panel wide">
                <div class="panel-head">
                  <h3>Create sample intake</h3>
                  <button id="loadSample">Load sample</button>
                </div>
                <textarea id="samplePayload" spellcheck="false">{sample_json}</textarea>
                <div class="actions">
                  <button id="createIntake">POST /intakes</button>
                  <button id="scoreAssessment">POST /assessments/score</button>
                </div>
              </article>

              <article class="panel">
                <h3>Admin queue</h3>
                <button id="loadQueue">GET /admin/queue</button>
                <ul id="queueList" class="queue-list"></ul>
              </article>

              <article class="panel wide">
                <h3>Operator views</h3>
                <div class="view-grid">{cards}</div>
              </article>

              <article class="panel output-panel">
                <h3>API response</h3>
                <pre id="output">Ready.</pre>
              </article>
            </section>
          </main>
        </div>
        <script>
          window.ADMIN_CONFIG = {json.dumps({'slug': slug, **cfg})};
        </script>
        <script src="./app.js"></script>
      </body>
    </html>
    '''


def css(cfg: dict) -> str:
    return f'''
    :root {{
      color-scheme: dark;
      --accent: {cfg['accent']};
      --bg: #08111f;
      --panel: rgba(15, 23, 42, 0.88);
      --panel-2: rgba(30, 41, 59, 0.72);
      --text: #e5eefc;
      --muted: #93a4bb;
      --border: rgba(148, 163, 184, 0.24);
    }}

    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background: radial-gradient(circle at top left, color-mix(in srgb, var(--accent) 24%, transparent), transparent 34rem), var(--bg);
    }}
    .shell {{ display: grid; grid-template-columns: 320px 1fr; min-height: 100vh; }}
    .sidebar {{ padding: 2rem; border-right: 1px solid var(--border); background: rgba(2, 6, 23, 0.72); }}
    .eyebrow {{ color: var(--accent); text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.74rem; font-weight: 800; }}
    h1, h2, h3, p {{ margin-top: 0; }}
    h1 {{ font-size: 1.85rem; line-height: 1.05; }}
    h2 {{ font-size: clamp(2rem, 4vw, 4rem); line-height: 0.98; margin-bottom: 1rem; }}
    .operator {{ color: var(--muted); }}
    nav {{ display: grid; gap: 0.65rem; margin: 2rem 0; }}
    button, input, textarea {{ font: inherit; }}
    button {{ border: 0; border-radius: 999px; padding: 0.8rem 1rem; background: var(--accent); color: #020617; font-weight: 800; cursor: pointer; }}
    .view-tab {{ background: var(--panel-2); color: var(--text); border: 1px solid var(--border); text-align: left; }}
    .api-box {{ display: grid; gap: 0.5rem; padding: 1rem; border: 1px solid var(--border); border-radius: 1rem; background: var(--panel); }}
    label {{ color: var(--muted); font-size: 0.85rem; }}
    input, textarea {{ width: 100%; border: 1px solid var(--border); border-radius: 0.85rem; background: #020617; color: var(--text); padding: 0.85rem; }}
    small {{ color: var(--muted); line-height: 1.4; }}
    main {{ padding: 2rem; }}
    .hero {{ display: flex; align-items: start; justify-content: space-between; gap: 1rem; padding: 2rem; border: 1px solid var(--border); border-radius: 1.5rem; background: linear-gradient(135deg, var(--panel), rgba(2, 6, 23, 0.42)); }}
    .hero p {{ color: var(--muted); max-width: 760px; }}
    .metrics {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1rem 0; }}
    .metrics article, .panel {{ padding: 1.25rem; border: 1px solid var(--border); border-radius: 1.2rem; background: var(--panel); box-shadow: 0 24px 70px rgba(0,0,0,0.22); }}
    .metrics span, .view-card span {{ color: var(--muted); display: block; font-size: 0.8rem; margin-bottom: 0.4rem; }}
    .metrics strong {{ display: block; min-height: 2.6rem; }}
    .metrics em {{ color: var(--accent); font-style: normal; font-weight: 900; }}
    .grid {{ display: grid; grid-template-columns: 1.4fr 0.8fr; gap: 1rem; }}
    .wide {{ grid-column: span 1; }}
    .panel-head, .actions {{ display: flex; justify-content: space-between; gap: 0.8rem; align-items: center; margin-bottom: 1rem; }}
    textarea {{ min-height: 240px; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    .view-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.8rem; }}
    .view-card {{ background: var(--panel-2); border: 1px solid var(--border); border-radius: 1rem; padding: 1rem; }}
    .view-card p {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 0; }}
    .queue-list {{ list-style: none; padding: 0; margin: 1rem 0 0; display: grid; gap: 0.65rem; }}
    .queue-list li {{ border: 1px solid var(--border); border-radius: 0.9rem; padding: 0.85rem; background: #020617; }}
    pre {{ white-space: pre-wrap; word-break: break-word; color: #c4d7f8; background: #020617; border-radius: 0.85rem; padding: 1rem; min-height: 240px; overflow: auto; }}
    @media (max-width: 960px) {{
      .shell {{ grid-template-columns: 1fr; }}
      .sidebar {{ border-right: 0; border-bottom: 1px solid var(--border); }}
      .metrics, .grid {{ grid-template-columns: 1fr; }}
      .hero {{ flex-direction: column; }}
    }}
    '''


def js(cfg: dict) -> str:
    sample = json.dumps({"message": cfg["sample"], "signals": cfg["signals"]}, indent=2)
    return f'''
    const config = window.ADMIN_CONFIG;
    const $ = (id) => document.getElementById(id);

    function baseUrl() {{
      return $("apiBase").value.replace(/\/$/, "");
    }}

    function writeOutput(data) {{
      $("output").textContent = typeof data === "string" ? data : JSON.stringify(data, null, 2);
    }}

    async function request(path, options = {{}}) {{
      const response = await fetch(`${{baseUrl()}}${{path}}`, {{
        headers: {{ "Content-Type": "application/json", ...(options.headers || {{}}) }},
        ...options,
      }});
      const text = await response.text();
      let data;
      try {{ data = text ? JSON.parse(text) : {{}}; }} catch {{ data = text; }}
      if (!response.ok) throw new Error(JSON.stringify(data, null, 2));
      return data;
    }}

    function buildIntakePayload() {{
      const raw = JSON.parse($("samplePayload").value);
      return {{
        source: "admin_panel_demo",
        contact_name: "Sample Operator Lead",
        contact_email: "sample@example.com",
        company_or_location: config.title,
        message: raw.message,
        signals: raw.signals || {{}},
        consent_for_followup: false,
      }};
    }}

    $("loadSample").addEventListener("click", () => {{
      $("samplePayload").value = {json.dumps(sample)};
      writeOutput("Sample payload loaded.");
    }});

    $("checkHealth").addEventListener("click", async () => {{
      try {{
        const [health, meta] = await Promise.all([request("/health"), request("/meta")]);
        $("apiStatus").textContent = health.status === "ok" ? "Healthy" : "Unexpected";
        $("primaryMetric").textContent = meta.expected_signals.length + " tracked signals";
        $("secondaryMetric").textContent = meta.ai_modules.length + " modules";
        writeOutput({{ health, meta }});
      }} catch (error) {{
        $("apiStatus").textContent = "Offline";
        writeOutput(`API check failed. Start FastAPI backend first.\n\n${{error.message}}`);
      }}
    }});

    $("createIntake").addEventListener("click", async () => {{
      try {{
        const data = await request("/intakes", {{ method: "POST", body: JSON.stringify(buildIntakePayload()) }});
        writeOutput(data);
      }} catch (error) {{ writeOutput(error.message); }}
    }});

    $("scoreAssessment").addEventListener("click", async () => {{
      try {{
        const payload = JSON.parse($("samplePayload").value);
        const data = await request("/assessments/score", {{ method: "POST", body: JSON.stringify(payload) }});
        writeOutput(data);
      }} catch (error) {{ writeOutput(error.message); }}
    }});

    $("loadQueue").addEventListener("click", async () => {{
      try {{
        const data = await request("/admin/queue");
        const list = $("queueList");
        list.innerHTML = "";
        if (!data.length) {{
          list.innerHTML = "<li>No queue items yet. Create a sample intake first.</li>";
        }} else {{
          data.forEach((item) => {{
            const li = document.createElement("li");
            li.innerHTML = `<strong>${{item.priority}}</strong><br>${{item.message_preview}}<br><small>${{item.next_action}}</small>`;
            list.appendChild(li);
          }});
        }}
        writeOutput(data);
      }} catch (error) {{ writeOutput(error.message); }}
    }});

    document.querySelectorAll(".view-tab").forEach((button) => {{
      button.addEventListener("click", () => writeOutput(`Selected admin view: ${{button.dataset.view}}`));
    }});
    '''


def readme(slug: str, cfg: dict) -> str:
    return f'''
    # {cfg['title']} — Admin Panel Frontend

    This folder now contains a lightweight operator/admin panel prototype for **{cfg['title']}**.

    ## Current status

    - Frontend type: dependency-free HTML/CSS/JS admin panel.
    - Backend target: local FastAPI app under `../backend`.
    - Database: none connected; backend uses in-memory repository until MongoDB is approved.
    - Purpose: let Andre inspect the admin workflow for each incubated business from GitHub and run it locally without a build step.

    ## Files

    ```text
    index.html
    styles.css
    app.js
    README.md
    ROUTES.md
    VIEWS.md
    ```

    ## Run locally

    Terminal 1:

    ```bash
    cd output/businesses/{slug}/backend
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8000
    ```

    Terminal 2:

    ```bash
    cd output/businesses/{slug}/admin
    python -m http.server 4173
    ```

    Open:

    ```text
    http://localhost:4173
    ```

    ## Admin views represented

    {chr(10).join(f'- {view}' for view in cfg['views'])}

    ## Connected API actions

    ```text
    GET  /health
    GET  /meta
    POST /intakes
    POST /assessments/score
    GET  /admin/queue
    ```

    ## Next step

    Once a business is chosen as the real MVP, replace this static prototype with either:

    - a React/Vite admin app, or
    - a shared admin shell package reused across all businesses.
    '''


def generate(slug: str, cfg: dict) -> None:
    admin = BASE / slug / "admin"
    write(admin / "index.html", html(slug, cfg))
    write(admin / "styles.css", css(cfg))
    write(admin / "app.js", js(cfg))
    write(admin / "README.md", readme(slug, cfg))


def main() -> None:
    for slug, cfg in BUSINESSES.items():
        generate(slug, cfg)
    print(f"Generated admin panel frontends for {len(BUSINESSES)} businesses.")


if __name__ == "__main__":
    main()
