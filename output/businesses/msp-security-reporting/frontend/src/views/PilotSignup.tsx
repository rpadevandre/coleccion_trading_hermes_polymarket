import { FormEvent, useState } from 'react';
import { businessMeta, qualificationSignals } from '../businessMeta';
import type { ViewProps } from '../App';

export default function PilotSignup({ onNavigate }: ViewProps) {
  const [company, setCompany] = useState('');
  const [pilotClient, setPilotClient] = useState('One anonymized manufacturing client');
  const [approver, setApprover] = useState('');
  const [urgency, setUrgency] = useState('Need renewal/QBR proof within 30 days');
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const canSubmit = company.trim().length > 2 && approver.includes('@') && pilotClient.trim().length > 8;

  const submitPilot = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!canSubmit) return;
    setLoading(true);
    window.setTimeout(() => {
      setLoading(false);
      setSubmitted(true);
    }, 500);
  };

  return (
    <main className="business-page">
      <section className="hero hero-grid">
        <div>
          <p className="eyebrow">Narrow pilot scope</p>
          <h1>Test one anonymized client report before building integrations.</h1>
          <p className="lede">The pilot CTA is intentionally specific: one MSP, one client, one month of redacted evidence, one human-approved report.</p>
        </div>
        <aside className="hero-panel">
          <strong>What success means</strong>
          <p>An MSP says the report is useful enough to show a client, save QBR prep time or support a renewal/security upsell conversation.</p>
        </aside>
      </section>

      <section className="section-grid two">
        <article className="card">
          <h2>Included in pilot</h2>
          <ul className="check-list">
            <li>Redacted evidence import checklist</li>
            <li>Draft executive summary and remediation narrative</li>
            <li>Approval screen with source citations</li>
            <li>Feedback call focused on willingness to pay</li>
          </ul>
        </article>
        <article className="card">
          <h2>Not included yet</h2>
          <ul className="x-list">
            <li>No production tenant connection</li>
            <li>No automated client delivery</li>
            <li>No secrets, credentials or real customer identifiers</li>
            <li>No unreviewed AI output</li>
          </ul>
        </article>
      </section>

      <form className="card form-card" onSubmit={submitPilot}>
        <h2>Pilot qualification</h2>
        <label>
          MSP / company name
          <input value={company} onChange={(event) => setCompany(event.target.value)} placeholder="Example: Northstar Managed IT" />
        </label>
        <label>
          Anonymized pilot client
          <input value={pilotClient} onChange={(event) => setPilotClient(event.target.value)} />
        </label>
        <label>
          Human approver email
          <input value={approver} onChange={(event) => setApprover(event.target.value)} placeholder="approver@msp.example" inputMode="email" />
        </label>
        <label>
          Why now?
          <textarea value={urgency} onChange={(event) => setUrgency(event.target.value)} />
        </label>

        <div className="qualification-box">
          <strong>Strong pilot if:</strong>
          <ul>
            {qualificationSignals.slice(0, 3).map((signal) => (
              <li key={signal}>{signal}</li>
            ))}
          </ul>
        </div>

        {loading && <div className="loading-state" role="status">Checking pilot fit from non-sensitive inputs…</div>}
        {!loading && !submitted && <button type="submit" disabled={!canSubmit}>Request one-report pilot</button>}
        {!loading && !submitted && !canSubmit && <p className="error-copy">Complete company, approver email and pilot-client description to enable the CTA.</p>}
        {submitted && (
          <div className="success-box" role="status">
            <h2>Pilot request captured</h2>
            <p>{businessMeta.shortName} would now prepare a redacted-evidence checklist and schedule human review before any report is generated.</p>
            <button type="button" className="secondary" onClick={() => onNavigate('landing', 'Completed pilot request and returned to overview')}>
              Back to overview
            </button>
          </div>
        )}
      </form>

      <section className="guardrail">
        <strong>Validation note:</strong> This prototype is optimized to measure buyer urgency, not collect sensitive customer records.
      </section>
    </main>
  );
}
