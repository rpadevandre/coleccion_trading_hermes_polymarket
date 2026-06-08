import { useMemo, useState } from 'react';
import type { ViewProps } from '../App';
import { frontendViews } from '../businessMeta';

const viewMeta = frontendViews.find((view) => view.key === 'audit') ?? frontendViews[3];

export default function FreeAuditForm({ onNavigate }: ViewProps) {
  const [form, setForm] = useState({
    email: '',
    company: '',
    techs: '5-10',
    missedCalls: '10-25',
    afterHours: 'Voicemail only',
    reviewer: '',
    notes: ''
  });

  const missingFields = useMemo(
    () => [
      ['Work email', form.email],
      ['Company name', form.company],
      ['Human reviewer', form.reviewer]
    ].filter(([, value]) => !value),
    [form]
  );

  const update = (field: keyof typeof form, value: string) => setForm((current) => ({ ...current, [field]: value }));

  return (
    <main className="business-page">
      <section className="hero">
        <p className="eyebrow">No-PII qualification form</p>
        <h1>{viewMeta.name}</h1>
        <p className="lede">{viewMeta.description}</p>
      </section>

      <section className="card form-card">
        <div className="card-header">
          <div>
            <h2>Audit request worksheet</h2>
            <p>Fields are operational only. The prototype should not ask for caller names, phone numbers or live recordings.</p>
          </div>
          <span className={missingFields.length ? 'badge warning' : 'badge ready'}>{missingFields.length ? `${missingFields.length} required left` : 'Ready for review'}</span>
        </div>
        <form className="stack" onSubmit={(event) => event.preventDefault()}>
          <label>Work email<input type="email" value={form.email} onChange={(event) => update('email', event.target.value)} placeholder="owner@hvacco.com" /></label>
          <label>Company name<input value={form.company} onChange={(event) => update('company', event.target.value)} placeholder="Bright Air Heating & Cooling" /></label>
          <div className="calc-grid">
            <label>Technician count<select value={form.techs} onChange={(event) => update('techs', event.target.value)}><option>1-4</option><option>5-10</option><option>11-25</option><option>25+</option></select></label>
            <label>Missed calls / week<select value={form.missedCalls} onChange={(event) => update('missedCalls', event.target.value)}><option>0-10</option><option>10-25</option><option>25-50</option><option>50+</option></select></label>
            <label>Current after-hours path<select value={form.afterHours} onChange={(event) => update('afterHours', event.target.value)}><option>Voicemail only</option><option>Answering service</option><option>Owner cell phone</option><option>CSR rotation</option></select></label>
          </div>
          <label>Who reviews urgent suggestions?<input value={form.reviewer} onChange={(event) => update('reviewer', event.target.value)} placeholder="Owner, dispatcher or service manager" /></label>
          <label>What is breaking now?<textarea value={form.notes} onChange={(event) => update('notes', event.target.value)} placeholder="Example: after-hours emergency calls are not separated from tune-up requests until the next morning." /></label>
          <div className="form-actions">
            <button type="button" disabled={missingFields.length > 0} onClick={() => onNavigate('pilot')}>{viewMeta.ctaLabel}</button>
            <button className="secondary" type="button" onClick={() => onNavigate('demo')}>Back to demo flow</button>
          </div>
        </form>
      </section>

      {missingFields.length > 0 ? (
        <section className="empty-state"><strong>Incomplete:</strong> add {missingFields.map(([label]) => label).join(', ')} before marking this audit as qualified.</section>
      ) : (
        <section className="success-state"><strong>Qualified:</strong> operational fit captured. Next CTA should confirm pilot authority and success metrics.</section>
      )}
    </main>
  );
}
