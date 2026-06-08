import React from 'react';
import { businessMeta, frontendViews } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'Landing') ?? {
  name: 'Landing',
  path: '/landing',
  description: 'Public validation page for restaurants.',
  primaryOutcome: 'Validate buyer demand and move qualified users into a pilot.'
};

export default function Landing() {
  return (
    <main className="business-page" style={{ '--accent': businessMeta.accent } as React.CSSProperties}>
      <section className="hero">
        <p className="eyebrow">{businessMeta.name}</p>
        <h1>{viewMeta.name}</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">{businessMeta.metric}</p>
      </section>

  <section className="card">
    <h2>How it works</h2>
    <ol>
      <li>Import or capture the workflow item.</li>
      <li>Classify, summarize and flag missing information.</li>
      <li>Route to the right human with an audit trail.</li>
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
