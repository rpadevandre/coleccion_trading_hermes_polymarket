export const businessMeta = {
    name: 'Law Firm Intake Triage',
    headline: 'Convert messy legal inquiries into attorney-ready intake summaries.',
    subheadline: 'Practice-area triage, missing-fact checklists and human review without giving legal advice.',
    accent: '#334155',
    metric: 'Cleaner intake before attorney review',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for law firms.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PracticeAreaDemo', path: '/practice-area-demo', description: 'Demo inquiry classification.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'IntakeQualityCalculator', path: '/intake-quality-calculator', description: 'Calculator for staff/attorney time saved.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'FirmAuditForm', path: '/firm-audit-form', description: 'Firm intake workflow audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot signup page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
