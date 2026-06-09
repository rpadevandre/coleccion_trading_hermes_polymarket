import type { CSSProperties, FormEvent } from 'react';
import { useMemo, useState } from 'react';
import { businessMeta, frontendViews } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'PilotSignup') ?? frontendViews[0];
const accentStyle = { '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties;

export default function PilotSignup() {
  const [owner, setOwner] = useState('');
  const [startWindow, setStartWindow] = useState('This month');
  const [successMetric, setSuccessMetric] = useState('Booked consults recovered');
  const [approvalOwner, setApprovalOwner] = useState('Front desk lead');
  const [acceptedGuardrail, setAcceptedGuardrail] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const canSubmit = useMemo(() => owner.trim().length > 1 && acceptedGuardrail, [owner, acceptedGuardrail]);

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!canSubmit) return;
    setSubmitted(true);
  }

  return (
    <main className="business-page" style={accentStyle}>
      <section className="hero compact-hero">
        <p className="eyebrow">14-day pilot offer</p>
        <h1>Prove recovered consult revenue before a long contract.</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">{viewMeta.buyerSignal}</p>
      </section>

      <section className="section-grid">
        <article className="card">
          <h2>Pilot scope</h2>
          <ol className="timeline-list">
            <li><strong>Day 1:</strong> map lead sources and approved follow-up language.</li>
            <li><strong>Days 2–10:</strong> review hot missed leads and staff-approved drafts daily.</li>
            <li><strong>Days 11–14:</strong> report booked consults, no-shows and revenue estimate.</li>
          </ol>
        </article>
        <form className="card stack" onSubmit={handleSubmit}>
          <h2>Reserve pilot review</h2>
          <label>Decision owner<input value={owner} onChange={(event) => setOwner(event.target.value)} placeholder="Owner, manager or lead coordinator" /></label>
          <label>Preferred start window<select value={startWindow} onChange={(event) => setStartWindow(event.target.value)}><option>This month</option><option>Next 30 days</option><option>After ad campaign launch</option></select></label>
          <label>Success metric<select value={successMetric} onChange={(event) => setSuccessMetric(event.target.value)}><option>Booked consults recovered</option><option>Response time reduced</option><option>Missed-call callbacks completed</option><option>Instagram DMs cleared</option></select></label>
          <label>Who approves messages?<input value={approvalOwner} onChange={(event) => setApprovalOwner(event.target.value)} /></label>
          <label className="checkbox-row"><input type="checkbox" checked={acceptedGuardrail} onChange={(event) => setAcceptedGuardrail(event.target.checked)} /> I understand this prototype uses human-approved drafts only.</label>
          {!canSubmit && <p className="empty-state">Add a decision owner and accept the human-approval guardrail to continue.</p>}
          <button type="submit" disabled={!canSubmit}>Request pilot fit review</button>
          {submitted && <p className="success-state">Pilot interest captured. Proposed scope: {startWindow}, measured by “{successMetric},” with {approvalOwner} approving follow-up.</p>}
        </form>
      </section>

      <section className="guardrail"><strong>Risk copy:</strong> Do not position this as medical automation. It is a revenue operations workflow for reviewed consult follow-up.</section>
    </main>
  );
}
