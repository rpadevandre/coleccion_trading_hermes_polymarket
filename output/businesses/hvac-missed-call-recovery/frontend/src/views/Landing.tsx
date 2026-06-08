import type { ViewProps } from '../App';
import { businessMeta, frontendViews } from '../businessMeta';

const viewMeta = frontendViews.find((view) => view.key === 'landing') ?? frontendViews[0];

export default function Landing({ onNavigate }: ViewProps) {
  return (
    <main className="business-page">
      <section className="hero hero-grid">
        <div>
          <p className="eyebrow">Buyer validation page · HVAC owners</p>
          <h1>{businessMeta.headline}</h1>
          <p className="lede">{businessMeta.subheadline}</p>
          <div className="hero-actions">
            <button type="button" onClick={() => onNavigate('roi')}>{viewMeta.ctaLabel}</button>
            <button className="secondary" type="button" onClick={() => onNavigate('demo')}>See the call flow</button>
          </div>
          <p className="risk-note">{businessMeta.riskCopy}</p>
        </div>
        <aside className="signal-card" aria-label="Revenue leakage validation metric">
          <span>Validation target</span>
          <strong>{businessMeta.metric}</strong>
          <p>{businessMeta.marketProof}</p>
        </aside>
      </section>

      <section className="section-grid three">
        {businessMeta.validationQuestions.map((question) => (
          <article className="card compact" key={question}>
            <h2>{question}</h2>
            <p>Use this prompt in sales calls to verify the pain before building deeper automation.</p>
          </article>
        ))}
      </section>

      <section className="card split-card">
        <div>
          <p className="eyebrow">What buyers get first</p>
          <h2>A manual leakage audit, not a premature integration project.</h2>
          <p>{businessMeta.buyerPromise}</p>
        </div>
        <ul className="check-list">
          {businessMeta.proofPoints.map((point) => <li key={point}>{point}</li>)}
        </ul>
      </section>

      <section className="guardrail">
        <strong>Buyer-validation copy:</strong> Ask for voicemail samples, call counts and routing preferences — never customer PII in this prototype.
      </section>
    </main>
  );
}
