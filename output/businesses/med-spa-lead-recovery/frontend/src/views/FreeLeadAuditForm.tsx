import type { CSSProperties, FormEvent } from 'react';
import { useMemo, useState } from 'react';
import { businessMeta, frontendViews, leadSources } from '../businessMeta';

type LeadSource = typeof leadSources[number];
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'FreeLeadAuditForm') ?? frontendViews[0];
const accentStyle = { '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties;

export default function FreeLeadAuditForm() {
  const [clinicName, setClinicName] = useState('');
  const [email, setEmail] = useState('');
  const [monthlyLeads, setMonthlyLeads] = useState('');
  const [source, setSource] = useState<LeadSource>(leadSources[0]);
  const [bottleneck, setBottleneck] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const isReady = useMemo(() => clinicName.trim() && email.includes('@') && monthlyLeads.trim() && bottleneck.trim(), [clinicName, email, monthlyLeads, bottleneck]);

  function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!isReady) return;
    setIsLoading(true);
    window.setTimeout(() => {
      setIsLoading(false);
      setSubmitted(true);
    }, 450);
  }

  return (
    <main className="business-page" style={accentStyle}>
      <section className="hero compact-hero">
        <p className="eyebrow">Free audit intake</p>
        <h1>Find the consult leads leaking from your med spa.</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">No PHI, screenshots or real patient names required.</p>
      </section>

      <section className="form-layout">
        <form className="card stack" onSubmit={handleSubmit}>
          <h2>Audit request</h2>
          <label>Clinic or practice name<input value={clinicName} onChange={(event) => setClinicName(event.target.value)} placeholder="Radiant Aesthetics" /></label>
          <label>Work email<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="owner@clinic.com" /></label>
          <label>Approx. new leads per month<input value={monthlyLeads} onChange={(event) => setMonthlyLeads(event.target.value)} placeholder="80 across Instagram, forms and calls" /></label>
          <label>Biggest lead source<select value={source} onChange={(event) => setSource(event.target.value as typeof leadSources[number])}>{leadSources.map((item) => <option key={item}>{item}</option>)}</select></label>
          <label>Where does follow-up break?<textarea value={bottleneck} onChange={(event) => setBottleneck(event.target.value)} placeholder="Example: DMs are checked twice a day and missed calls are returned after lunch." /></label>
          {!isReady && <p className="empty-state">Complete the required fields to unlock the audit request CTA.</p>}
          <button type="submit" disabled={!isReady || isLoading}>{isLoading ? 'Preparing audit request…' : 'Request my free lead leak audit'}</button>
          {submitted && <p className="success-state">Audit request captured for {clinicName}. Next prototype step: show a booking calendar or concierge handoff.</p>}
        </form>

        <aside className="card">
          <h2>What the audit returns</h2>
          <ul className="check-list">
            <li>Estimated lost consult value by source.</li>
            <li>Suggested response SLA for high-intent treatments.</li>
            <li>Example staff-approved follow-up templates.</li>
            <li>Recommendation on whether a 14-day pilot is worth testing.</li>
          </ul>
          <p className="helper-text">Error-state copy: if submission fails, ask the buyer to email anonymized lead counts instead of retrying with sensitive data.</p>
        </aside>
      </section>

      <section className="guardrail"><strong>Validation guardrail:</strong> Collect workflow metadata only. Do not request patient names, photos, medical history or treatment records.</section>
    </main>
  );
}
