import { businessMeta, sampleEvidence, qualificationSignals } from '../businessMeta';
import type { ViewProps } from '../App';

export default function Landing({ onNavigate }: ViewProps) {
  return (
    <main className="business-page">
      <section className="hero hero-grid">
        <div>
          <p className="eyebrow">Validation prototype • no client data required</p>
          <h1>{businessMeta.headline}</h1>
          <p className="lede">{businessMeta.subheadline}</p>
          <div className="hero-actions">
            <button type="button" onClick={() => onNavigate('stack-audit-form', 'Clicked stack audit from landing hero')}>
              Audit my reporting workflow
            </button>
            <button type="button" className="secondary" onClick={() => onNavigate('report-before-after', 'Wants to compare raw tool noise against report output')}>
              See before / after
            </button>
          </div>
        </div>
        <aside className="hero-panel">
          <span className="metric">{businessMeta.metric}</span>
          <p>{businessMeta.promise}</p>
        </aside>
      </section>

      <section className="section-grid three">
        {businessMeta.proofPoints.map((point) => (
          <article className="card" key={point}>
            <h2>Buyer pain signal</h2>
            <p>{point}</p>
          </article>
        ))}
      </section>

      <section className="card split-card">
        <div>
          <p className="eyebrow">Sample evidence queue</p>
          <h2>What the prototype understands</h2>
          <p className="muted">These are anonymized examples only. The goal is to prove MSP demand before connecting any production system.</p>
        </div>
        <div className="evidence-list">
          {sampleEvidence.map((item) => (
            <article className="evidence-item" key={item.source}>
              <strong>{item.tool}</strong>
              <span>{item.source}</span>
              <p>{item.executive}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <h2>Good-fit pilot signals</h2>
        <ul className="check-list">
          {qualificationSignals.map((signal) => (
            <li key={signal}>{signal}</li>
          ))}
        </ul>
        <button type="button" onClick={() => onNavigate('pilot-signup', 'Meets at least one pilot qualification signal')}>
          Check pilot fit
        </button>
      </section>

      <section className="guardrail">
        <strong>Buyer-validation copy:</strong> We are validating willingness to pay for faster MSP reporting, not asking for secrets. Use fake names, screenshots with redactions or exported summaries.
      </section>
    </main>
  );
}
