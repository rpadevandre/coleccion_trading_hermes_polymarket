import type { ViewProps } from '../App';
import { businessMeta, frontendViews } from '../businessMeta';

const viewMeta = frontendViews.find((view) => view.key === 'demo') ?? frontendViews[2];

const stages = [
  { title: '1. Capture', body: 'Missed voicemail or manual transcript is entered with caller name, callback number, ZIP and rough issue.', state: 'Loading state: transcript import pending until a human confirms source.' },
  { title: '2. Classify', body: 'AI suggests Emergency, Quote, Maintenance, Retention or Spam with confidence and missing-field flags.', state: 'Error state: low confidence pauses all routing and asks dispatcher to review.' },
  { title: '3. Route', body: 'Urgent calls go to owner/on-call tech; quotes go to estimator; retention goes to CSR queue.', state: 'Empty state: if no rules match, hold in Needs Human Review.' },
  { title: '4. Prove ROI', body: 'Outcome is logged as booked, follow-up, not-serviceable or lost competitor job for weekly revenue reporting.', state: 'Success state: booked jobs roll into recovered revenue metrics.' }
];

export default function DemoCallFlow({ onNavigate }: ViewProps) {
  return (
    <main className="business-page">
      <section className="hero">
        <p className="eyebrow">Concierge demo, no production integration</p>
        <h1>{viewMeta.name}</h1>
        <p className="lede">{viewMeta.description}</p>
        <button type="button" onClick={() => onNavigate('audit')}>{viewMeta.ctaLabel}</button>
      </section>

      <section className="flow-board" aria-label="Missed-call recovery workflow">
        {stages.map((stage) => (
          <article className="flow-step" key={stage.title}>
            <h2>{stage.title}</h2>
            <p>{stage.body}</p>
            <small>{stage.state}</small>
          </article>
        ))}
      </section>

      <section className="card">
        <div className="card-header">
          <div>
            <p className="eyebrow">Sample queue</p>
            <h2>What the owner sees before dispatch</h2>
          </div>
          <span className="badge">3 review items</span>
        </div>
        <div className="queue-list">
          {businessMeta.sampleCalls.map((call) => (
            <article className="queue-item" key={call.caller}>
              <div>
                <strong>{call.caller}</strong>
                <p>{call.issue}</p>
              </div>
              <span>{call.urgency}</span>
              <span>{call.route}</span>
              <em>{call.value}</em>
            </article>
          ))}
        </div>
      </section>

      <section className="guardrail"><strong>Human-in-loop:</strong> Demo language explicitly says “suggested route” until the dispatcher approves the item.</section>
    </main>
  );
}
