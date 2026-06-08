import React from 'react';
import { businessMeta, frontendViews } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'EventInquiryDemo') ?? {
  name: 'EventInquiryDemo',
  path: '/event-inquiry-demo',
  description: 'Demo inquiry parsing.',
  primaryOutcome: 'Validate buyer demand and move qualified users into a pilot.'
};

export default function EventInquiryDemo() {
  return (
    <main className="business-page" style={{ '--accent': businessMeta.accent } as React.CSSProperties}>
      <section className="hero">
        <p className="eyebrow">{businessMeta.name}</p>
        <h1>{viewMeta.name}</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">{businessMeta.metric}</p>
      </section>

  <section className="card">
    <h2>Demo sequence</h2>
    <ol>
      <li>Capture source event or message.</li>
      <li>AI extracts structured fields with confidence.</li>
      <li>Human reviews suggested action.</li>
      <li>Admin panel tracks outcome and audit trail.</li>
    </ol>
  </section>

  <section className="card">
    <h2>Primary outcome</h2>
    <p>{viewMeta.primaryOutcome}</p>
  </section>

  <section className="card">
    <h2>CTA</h2>
    <button type="button">Book a workflow audit</button>
  </section>
      <section className="guardrail">
        <strong>Human-in-loop:</strong> AI suggestions stay reviewable, auditable and reversible before any customer-facing action.
      </section>
    </main>
  );
}
