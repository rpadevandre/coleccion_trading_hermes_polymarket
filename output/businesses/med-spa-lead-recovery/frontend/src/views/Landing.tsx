import type { CSSProperties } from 'react';
import { businessMeta, frontendViews, proofPoints, treatmentLines } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'Landing') ?? frontendViews[0];
const accentStyle = { '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties;

export default function Landing() {
  return (
    <main className="business-page" style={accentStyle}>
      <section className="hero split-hero">
        <div>
          <p className="eyebrow">Buyer-validation prototype</p>
          <h1>{businessMeta.headline}</h1>
          <p className="lede">{businessMeta.subheadline}</p>
          <div className="cta-row">
            <a className="button-link" href="#audit-intake">{businessMeta.primaryCta}</a>
            <a className="button-link secondary" href="#proof">{businessMeta.secondaryCta}</a>
          </div>
        </div>
        <aside className="hero-panel" aria-label="Lead recovery snapshot">
          <span className="metric">{businessMeta.metric}</span>
          <strong>$18k–$42k</strong>
          <p>Typical monthly consult value at risk for a clinic with 15–35 unanswered or slow-replied leads.</p>
        </aside>
      </section>

      <section className="section-grid" id="proof">
        <article className="card emphasis-card">
          <p className="eyebrow">Who this validates</p>
          <h2>{businessMeta.targetBuyer}</h2>
          <p>{viewMeta.description}</p>
        </article>
        <article className="card">
          <h2>Why clinics feel the pain now</h2>
          <ul className="check-list">
            <li>Instagram inquiries arrive after hours and get buried under content engagement.</li>
            <li>Front desk teams prioritize in-office patients before high-value consult follow-up.</li>
            <li>Owners know ads generate leads, but not which missed conversations cost bookings.</li>
          </ul>
        </article>
      </section>

      <section className="card">
        <div className="section-heading">
          <p className="eyebrow">Treatment value examples</p>
          <h2>Turn vague “lead follow-up” into revenue math.</h2>
        </div>
        <div className="treatment-grid">
          {treatmentLines.map((line) => (
            <div className="mini-card" key={line.name}>
              <strong>{line.name}</strong>
              <span>${line.value.toLocaleString()} avg.</span>
              <p>{line.examples}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="card" id="audit-intake">
        <div className="section-heading">
          <p className="eyebrow">Buyer signals this page should create</p>
          <h2>{viewMeta.primaryOutcome}</h2>
        </div>
        <div className="proof-list">
          {proofPoints.map((point) => (
            <div className="proof-row" key={point}>{point}</div>
          ))}
        </div>
      </section>

      <section className="guardrail">
        <strong>Compliance guardrail:</strong> {businessMeta.complianceNote}
      </section>
    </main>
  );
}
