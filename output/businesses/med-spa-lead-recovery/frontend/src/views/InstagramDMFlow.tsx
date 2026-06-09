import type { CSSProperties } from 'react';
import { useState } from 'react';
import { businessMeta, frontendViews, sampleLeads } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'InstagramDMFlow') ?? frontendViews[0];
const accentStyle = { '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties;

export default function InstagramDMFlow() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const selectedLead = sampleLeads[selectedIndex];

  return (
    <main className="business-page" style={accentStyle}>
      <section className="hero compact-hero">
        <p className="eyebrow">No real customer data demo</p>
        <h1>DM, form and missed-call recovery flow</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">{viewMeta.primaryOutcome}</p>
      </section>

      <section className="flow-layout">
        <div className="card">
          <h2>Sample lead queue</h2>
          <div className="lead-list">
            {sampleLeads.map((lead, index) => (
              <button className={index === selectedIndex ? 'lead-card selected' : 'lead-card'} type="button" key={lead.intent} onClick={() => setSelectedIndex(index)}>
                <span>{lead.source}</span>
                <strong>{lead.intent}</strong>
                <small>{lead.age} • {lead.value} • {lead.risk} risk</small>
              </button>
            ))}
          </div>
        </div>

        <div className="card review-card">
          <p className="eyebrow">Coordinator review</p>
          <h2>{selectedLead.intent}</h2>
          <dl className="detail-list">
            <div><dt>Source</dt><dd>{selectedLead.source}</dd></div>
            <div><dt>Age</dt><dd>{selectedLead.age}</dd></div>
            <div><dt>Estimated value</dt><dd>{selectedLead.value}</dd></div>
            <div><dt>Booking risk</dt><dd>{selectedLead.risk}</dd></div>
          </dl>
          <label className="draft-box">Human-approved draft<textarea value={selectedLead.draft} readOnly /></label>
          <div className="cta-row">
            <button type="button">Approve draft</button>
            <button className="secondary-button" type="button">Ask AI to revise</button>
          </div>
          <p className="helper-text">Empty state copy: when there are no leads, show “Connect a source or upload anonymized counts to preview recovery tasks.”</p>
        </div>
      </section>

      <section className="guardrail"><strong>Safety state:</strong> Drafts are suggestions for staff. The prototype intentionally avoids sending messages or making treatment claims.</section>
    </main>
  );
}
