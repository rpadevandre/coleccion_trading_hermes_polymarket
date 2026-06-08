export const businessMeta = {
    name: 'Dental Insurance Checklist',
    headline: 'Give dental teams a safer insurance verification checklist.',
    subheadline: 'Procedure-specific verification steps with human review and PHI-conscious workflows.',
    accent: '#0891b2',
    metric: 'Reduce verification rework and missed fields',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for dental offices.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ChecklistDemo', path: '/checklist-demo', description: 'Demo procedure-specific checklist.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ReworkCalculator', path: '/rework-calculator', description: 'Calculator for verification admin rework.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'OfficeAuditForm', path: '/office-audit-form', description: 'Office workflow audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Controlled pilot signup page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
