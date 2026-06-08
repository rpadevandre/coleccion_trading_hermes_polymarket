import React from 'react';
import { businessMeta, frontendViews } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'PipelineCalculator') ?? {
  name: 'PipelineCalculator',
  path: '/pipeline-calculator',
  description: 'Calculator for admin hours and bid throughput.',
  primaryOutcome: 'Validate buyer demand and move qualified users into a pilot.'
};

export default function PipelineCalculator() {
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

  <section className="card interactive-card">
    <h2>Quick estimate</h2>
    <div className="calc-grid">
      <label>Weekly volume<input type="number" defaultValue={25} /></label>
      <label>Average value<input type="number" defaultValue={750} /></label>
      <label>Recovery rate<input type="number" defaultValue={20} /></label>
    </div>
    <p className="result">Use this in the first MVP to calculate estimated recovered value before asking for a demo.</p>
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
