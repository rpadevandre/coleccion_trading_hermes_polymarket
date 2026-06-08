import { useMemo, useState } from 'react';
import type { ViewProps } from '../App';
import { businessMeta, frontendViews } from '../businessMeta';

const viewMeta = frontendViews.find((view) => view.key === 'pilot') ?? frontendViews[4];

const commitments = [
  'One accountable human approves urgent routing decisions.',
  'Pilot success is measured by booked callbacks, not vanity AI volume.',
  'Prototype uses anonymized call categories and manually entered summaries first.'
];

export default function PilotSignup({ onNavigate }: ViewProps) {
  const [authority, setAuthority] = useState('Owner');
  const [successMetric, setSuccessMetric] = useState('Booked emergency callbacks');
  const [timeline, setTimeline] = useState('This month');

  const readyCopy = useMemo(() => {
    if (timeline === 'Exploring only') return 'Discovery only: keep this buyer in validation interviews before offering a pilot.';
    return `${authority} can evaluate a pilot focused on ${successMetric.toLowerCase()} ${timeline.toLowerCase()}.`;
  }, [authority, successMetric, timeline]);

  return (
    <main className="business-page">
      <section className="hero hero-grid">
        <div>
          <p className="eyebrow">Pilot conversion</p>
          <h1>{viewMeta.name}</h1>
          <p className="lede">{viewMeta.description}</p>
          <div className="hero-actions">
            <button type="button">{viewMeta.ctaLabel}</button>
            <button className="secondary" type="button" onClick={() => onNavigate('audit')}>Edit audit details</button>
          </div>
        </div>
        <aside className="signal-card"><span>30-day pilot promise</span><strong>{businessMeta.buyerPromise}</strong></aside>
      </section>

      <section className="section-grid two">
        <article className="card">
          <h2>Qualification checkpoints</h2>
          <form className="stack" onSubmit={(event) => event.preventDefault()}>
            <label>Decision-maker<select value={authority} onChange={(event) => setAuthority(event.target.value)}><option>Owner</option><option>Operations manager</option><option>Dispatcher lead</option><option>Marketing manager</option></select></label>
            <label>Primary success metric<select value={successMetric} onChange={(event) => setSuccessMetric(event.target.value)}><option>Booked emergency callbacks</option><option>Replacement quote follow-up</option><option>Maintenance-plan retention</option><option>Reduced morning voicemail backlog</option></select></label>
            <label>Timeline<select value={timeline} onChange={(event) => setTimeline(event.target.value)}><option>This month</option><option>Next 30 days</option><option>Peak season only</option><option>Exploring only</option></select></label>
          </form>
        </article>

        <article className="card outcome-card">
          <p className="eyebrow">Readiness state</p>
          <h2>{timeline === 'Exploring only' ? 'Not pilot-ready yet' : 'Pilot-ready signal'}</h2>
          <p>{readyCopy}</p>
          <button type="button" disabled={timeline === 'Exploring only'}>{timeline === 'Exploring only' ? 'Keep in discovery' : 'Reserve pilot review'}</button>
        </article>
      </section>

      <section className="card">
        <h2>Concierge pilot rules</h2>
        <ul className="check-list">
          {commitments.map((item) => <li key={item}>{item}</li>)}
        </ul>
      </section>

      <section className="guardrail"><strong>Do not deploy:</strong> This page is validation copy and local React prototype only; no production CRM, telephony or SMS integration is implied.</section>
    </main>
  );
}
