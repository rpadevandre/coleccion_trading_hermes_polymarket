import { useState } from 'react';
import { sampleEvidence } from '../businessMeta';
import type { ViewProps } from '../App';

const approvalSteps = ['Evidence imported', 'AI draft ready', 'MSP edits language', 'Client export approved'];

export default function ClientProofDemo({ onNavigate }: ViewProps) {
  const [activeStep, setActiveStep] = useState(1);
  const selectedEvidence = sampleEvidence[Math.min(activeStep, sampleEvidence.length - 1)];
  const isApproved = activeStep === approvalSteps.length - 1;

  return (
    <main className="business-page">
      <section className="hero hero-grid">
        <div>
          <p className="eyebrow">Human-in-loop workflow</p>
          <h1>Draft faster, but never send unapproved AI language to a client.</h1>
          <p className="lede">
            This demo validates a core trust question: will MSPs use AI reporting if every paragraph shows source evidence, edit status and explicit approval?
          </p>
        </div>
        <aside className="status-card">
          <span className={isApproved ? 'status success' : 'status pending'}>{isApproved ? 'Ready to export' : 'Review required'}</span>
          <strong>{approvalSteps[activeStep]}</strong>
          <p>{isApproved ? 'Client-facing PDF is unlocked after human approval.' : 'Export remains disabled until an MSP approves the narrative.'}</p>
        </aside>
      </section>

      <section className="card">
        <h2>Approval timeline</h2>
        <div className="stepper">
          {approvalSteps.map((step, index) => (
            <button
              type="button"
              key={step}
              className={index === activeStep ? 'step active-step' : 'step'}
              onClick={() => setActiveStep(index)}
            >
              <span>{index + 1}</span>
              {step}
            </button>
          ))}
        </div>
      </section>

      <section className="demo-grid">
        <article className="card">
          <p className="eyebrow">Source evidence</p>
          <h2>{selectedEvidence.tool}: {selectedEvidence.source}</h2>
          <code className="block-code">{selectedEvidence.raw}</code>
          <p className="muted">No credentials, tenant names or real endpoints are needed for this prototype.</p>
        </article>
        <article className="card">
          <p className="eyebrow">Suggested client wording</p>
          <h2>Editable report paragraph</h2>
          <textarea value={selectedEvidence.executive} readOnly aria-label="Suggested report paragraph" />
          <div className="button-row">
            <button type="button" onClick={() => setActiveStep(3)}>Approve wording</button>
            <button type="button" className="secondary" onClick={() => setActiveStep(2)}>Needs edit</button>
          </div>
        </article>
      </section>

      <section className={isApproved ? 'success-box' : 'empty-state'}>
        <h2>{isApproved ? 'Export unlocked' : 'Export locked until approval'}</h2>
        <p>{isApproved ? 'A report export would now include the approved paragraph and source citation.' : 'This state reassures buyers that AI cannot silently send unsupported claims.'}</p>
        <button type="button" disabled={!isApproved} onClick={() => onNavigate('pilot-signup', 'Approved demo paragraph and wants pilot details')}>
          Continue to pilot signup
        </button>
      </section>
    </main>
  );
}
