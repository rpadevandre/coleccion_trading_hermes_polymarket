import type { CSSProperties } from 'react';
import { useMemo, useState } from 'react';
import { businessMeta, frontendViews, treatmentLines } from '../businessMeta';
import '../styles.css';

const viewMeta = frontendViews.find((view) => view.name === 'LeadLeakCalculator') ?? frontendViews[0];
const accentStyle = { '--accent': businessMeta.accent, '--accent-dark': businessMeta.accentDark } as CSSProperties;

export default function LeadLeakCalculator() {
  const [weeklyLeads, setWeeklyLeads] = useState(18);
  const [missRate, setMissRate] = useState(35);
  const [avgValue, setAvgValue] = useState(900);
  const [recoveryRate, setRecoveryRate] = useState(25);

  const result = useMemo(() => {
    const missedMonthly = Math.round(weeklyLeads * 4.33 * (missRate / 100));
    const recoverable = Math.round(missedMonthly * (recoveryRate / 100));
    const recoveredValue = recoverable * avgValue;
    return { missedMonthly, recoverable, recoveredValue };
  }, [weeklyLeads, missRate, avgValue, recoveryRate]);

  const hasEmptyInputs = weeklyLeads <= 0 || avgValue <= 0;

  return (
    <main className="business-page" style={accentStyle}>
      <section className="hero compact-hero">
        <p className="eyebrow">{businessMeta.name}</p>
        <h1>Lead leak calculator</h1>
        <p className="lede">{viewMeta.description}</p>
        <p className="metric">Buyer signal: {viewMeta.buyerSignal}</p>
      </section>

      <section className="card interactive-card">
        <div className="section-heading">
          <p className="eyebrow">Fast revenue model</p>
          <h2>Estimate value trapped in slow replies.</h2>
        </div>
        <div className="calc-grid">
          <label>New leads per week<input type="number" min="0" value={weeklyLeads} onChange={(event) => setWeeklyLeads(Number(event.target.value))} /></label>
          <label>Leads missed or replied late (%)<input type="number" min="0" max="100" value={missRate} onChange={(event) => setMissRate(Number(event.target.value))} /></label>
          <label>Average consult value ($)<input type="number" min="0" value={avgValue} onChange={(event) => setAvgValue(Number(event.target.value))} /></label>
          <label>Conservative recovery target (%)<input type="number" min="0" max="100" value={recoveryRate} onChange={(event) => setRecoveryRate(Number(event.target.value))} /></label>
        </div>

        {hasEmptyInputs ? (
          <p className="empty-state">Enter weekly lead volume and average consult value to calculate a recovery estimate.</p>
        ) : (
          <div className="result-panel" aria-live="polite">
            <div><span>Missed monthly leads</span><strong>{result.missedMonthly}</strong></div>
            <div><span>Recoverable consults</span><strong>{result.recoverable}</strong></div>
            <div><span>Monthly value at stake</span><strong>${result.recoveredValue.toLocaleString()}</strong></div>
          </div>
        )}
      </section>

      <section className="card">
        <h2>Use a real treatment mix during validation.</h2>
        <div className="treatment-grid">
          {treatmentLines.map((line) => (
            <button className="option-card" type="button" key={line.name} onClick={() => setAvgValue(line.value)}>
              <strong>{line.name}</strong>
              <span>${line.value.toLocaleString()}</span>
              <small>{line.examples}</small>
            </button>
          ))}
        </div>
      </section>

      <section className="guardrail"><strong>Buyer-validation copy:</strong> If this number feels real, the next step is a free audit using anonymized counts only — no patient records or screenshots required.</section>
    </main>
  );
}
