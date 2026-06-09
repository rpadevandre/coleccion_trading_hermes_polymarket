import { sampleEvidence, reportSections } from '../businessMeta';
import type { ViewProps } from '../App';

export default function ReportBeforeAfter({ onNavigate }: ViewProps) {
  return (
    <main className="business-page">
      <section className="hero">
        <p className="eyebrow">Raw technical noise vs. client-ready proof</p>
        <h1>Make invisible security work understandable enough to approve.</h1>
        <p className="lede">
          MSP clients rarely see the alerts closed, policies tightened and backup checks completed. This page validates whether a before/after report sample creates urgency.
        </p>
      </section>

      <section className="compare-grid">
        <article className="card raw-card">
          <p className="eyebrow">Before: tool output</p>
          <h2>Hard to sell in a QBR</h2>
          {sampleEvidence.map((item) => (
            <div className="raw-snippet" key={item.raw}>
              <strong>{item.tool}</strong>
              <code>{item.raw}</code>
            </div>
          ))}
        </article>

        <article className="card polished-card">
          <p className="eyebrow">After: approved narrative</p>
          <h2>Ready for an owner conversation</h2>
          {sampleEvidence.map((item) => (
            <div className="approved-snippet" key={item.executive}>
              <span>{item.status}</span>
              <p>{item.executive}</p>
            </div>
          ))}
        </article>
      </section>

      <section className="card">
        <h2>Report sections buyers can validate</h2>
        <div className="pill-row">
          {reportSections.map((section) => (
            <span className="pill" key={section}>{section}</span>
          ))}
        </div>
        <p className="muted">Each section keeps a visible source trail so the MSP can edit, reject or approve the AI summary before export.</p>
      </section>

      <section className="cta-band">
        <div>
          <h2>Would this help close renewals or reduce “what do we pay you for?” questions?</h2>
          <p>Continue to the approval demo or request a stack audit with anonymized evidence.</p>
        </div>
        <div className="button-row">
          <button type="button" onClick={() => onNavigate('client-proof-demo', 'Interested in human approval flow after before/after sample')}>
            Review approval flow
          </button>
          <button type="button" className="secondary" onClick={() => onNavigate('stack-audit-form', 'Wants own stack mapped to report sections')}>
            Map my stack
          </button>
        </div>
      </section>
    </main>
  );
}
