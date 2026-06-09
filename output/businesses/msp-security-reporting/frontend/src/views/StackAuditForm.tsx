import { FormEvent, useMemo, useState } from 'react';
import { businessMeta } from '../businessMeta';
import type { ViewProps } from '../App';

const initialTools = Object.fromEntries(businessMeta.stackOptions.map((tool) => [tool, false])) as Record<string, boolean>;

export default function StackAuditForm({ onNavigate }: ViewProps) {
  const [tools, setTools] = useState(initialTools);
  const [clientCount, setClientCount] = useState(25);
  const [hoursPerMonth, setHoursPerMonth] = useState(12);
  const [reportPain, setReportPain] = useState('Clients ask what security work was completed, but evidence is scattered across tools.');
  const [email, setEmail] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const selectedTools = useMemo(() => Object.entries(tools).filter(([, checked]) => checked).map(([tool]) => tool), [tools]);
  const estimatedMonthlyDrag = Math.max(0, clientCount * hoursPerMonth);
  const canSubmit = email.includes('@') && selectedTools.length > 0 && reportPain.trim().length > 20;

  const submitAudit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!canSubmit) return;
    setSubmitted(true);
  };

  return (
    <main className="business-page">
      <section className="hero">
        <p className="eyebrow">No-secrets intake</p>
        <h1>Map the MSP stack before asking for a pilot.</h1>
        <p className="lede">This form captures buyer-validation signal: tools used, report workload, urgency and whether the prospect can provide anonymized evidence.</p>
      </section>

      <form className="card form-card" onSubmit={submitAudit}>
        <h2>Reporting workflow audit</h2>
        <label>
          Work email
          <input value={email} onChange={(event) => setEmail(event.target.value)} placeholder="owner@msp.example" inputMode="email" />
        </label>

        <div className="calc-grid">
          <label>
            Managed clients
            <input type="number" min="1" value={clientCount} onChange={(event) => setClientCount(Number(event.target.value))} />
          </label>
          <label>
            Reporting hours / client / month
            <input type="number" min="0" value={hoursPerMonth} onChange={(event) => setHoursPerMonth(Number(event.target.value))} />
          </label>
          <div className="result-card">
            <span>Estimated monthly drag</span>
            <strong>{estimatedMonthlyDrag} hours</strong>
          </div>
        </div>

        <fieldset>
          <legend>Which tools create report evidence?</legend>
          <div className="checkbox-grid">
            {businessMeta.stackOptions.map((tool) => (
              <label className="checkbox-card" key={tool}>
                <input
                  type="checkbox"
                  checked={tools[tool]}
                  onChange={(event) => setTools((current) => ({ ...current, [tool]: event.target.checked }))}
                />
                {tool}
              </label>
            ))}
          </div>
        </fieldset>

        <label>
          What breaks in the current reporting workflow?
          <textarea value={reportPain} onChange={(event) => setReportPain(event.target.value)} />
        </label>

        {!canSubmit && (
          <div className="empty-state" role="status">
            Add a valid email, pick at least one evidence source and describe the reporting pain in 20+ characters.
          </div>
        )}

        {submitted ? (
          <div className="success-box" role="status">
            <h2>Audit request staged</h2>
            <p>Prototype success state: a real implementation would send only this non-sensitive stack summary for review.</p>
            <button type="button" onClick={() => onNavigate('pilot-signup', 'Submitted no-secrets stack audit and is ready for pilot scope')}>
              Continue to pilot scope
            </button>
          </div>
        ) : (
          <button type="submit" disabled={!canSubmit}>Request no-secrets audit</button>
        )}
      </form>
    </main>
  );
}
