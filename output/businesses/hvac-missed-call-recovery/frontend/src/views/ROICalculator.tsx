import { useMemo, useState } from 'react';
import type { ViewProps } from '../App';
import { businessMeta, frontendViews } from '../businessMeta';

const viewMeta = frontendViews.find((view) => view.key === 'roi') ?? frontendViews[1];

export default function ROICalculator({ onNavigate }: ViewProps) {
  const [missedCalls, setMissedCalls] = useState(18);
  const [averageTicket, setAverageTicket] = useState(950);
  const [closeRate, setCloseRate] = useState(32);
  const [recoveryRate, setRecoveryRate] = useState(45);

  const estimate = useMemo(() => {
    const monthlyCalls = missedCalls * 4.33;
    const qualifiedCalls = monthlyCalls * (closeRate / 100);
    const recoveredJobs = qualifiedCalls * (recoveryRate / 100);
    const recoveredRevenue = recoveredJobs * averageTicket;
    return {
      monthlyCalls: Math.round(monthlyCalls),
      recoveredJobs: recoveredJobs.toFixed(1),
      recoveredRevenue: Math.round(recoveredRevenue)
    };
  }, [averageTicket, closeRate, missedCalls, recoveryRate]);

  return (
    <main className="business-page">
      <section className="hero">
        <p className="eyebrow">Interactive buyer math</p>
        <h1>{viewMeta.name}</h1>
        <p className="lede">{viewMeta.description}</p>
      </section>

      <section className="card interactive-card">
        <div className="card-header">
          <div>
            <h2>Estimate monthly recoverable revenue</h2>
            <p>Defaults are intentionally conservative for a small HVAC operator during normal season.</p>
          </div>
          <button type="button" onClick={() => onNavigate('audit')}>{viewMeta.ctaLabel}</button>
        </div>

        <div className="calc-grid">
          <label>Missed calls / week<input type="number" min={0} value={missedCalls} onChange={(event) => setMissedCalls(Number(event.target.value))} /></label>
          <label>Average booked job value<input type="number" min={0} value={averageTicket} onChange={(event) => setAverageTicket(Number(event.target.value))} /></label>
          <label>Calls that could become jobs (%)<input type="number" min={0} max={100} value={closeRate} onChange={(event) => setCloseRate(Number(event.target.value))} /></label>
          <label>Realistic recovery rate (%)<input type="number" min={0} max={100} value={recoveryRate} onChange={(event) => setRecoveryRate(Number(event.target.value))} /></label>
        </div>

        <div className="result-grid" aria-live="polite">
          <div><span>Missed calls / month</span><strong>{estimate.monthlyCalls}</strong></div>
          <div><span>Recovered jobs / month</span><strong>{estimate.recoveredJobs}</strong></div>
          <div><span>Potential recovered value</span><strong>${estimate.recoveredRevenue.toLocaleString()}</strong></div>
        </div>

        {estimate.recoveredRevenue === 0 ? (
          <p className="empty-state">Enter call volume and ticket values to see whether an audit is worth prioritizing.</p>
        ) : (
          <p className="success-state">If the estimate is above $3k/month, the next validation step is a no-PII missed-call audit worksheet.</p>
        )}
      </section>

      <section className="guardrail"><strong>Guardrail:</strong> The estimate is directional sales discovery, not a guaranteed revenue claim.</section>
    </main>
  );
}
