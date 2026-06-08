export const businessMeta = {
    name: 'Med Spa Lead Recovery',
    headline: 'Recover med-spa leads before they book somewhere else.',
    subheadline: 'AI-assisted lead capture and human-approved consult follow-up for aesthetic clinics.',
    accent: '#db2777',
    metric: 'Booked consults recovered from slow replies',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for med spas.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'LeadLeakCalculator', path: '/lead-leak-calculator', description: 'Calculator for lost consult value.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'InstagramDMFlow', path: '/instagram-d-m-flow', description: 'Demo DM/form/call to consult flow.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'FreeLeadAuditForm', path: '/free-lead-audit-form', description: 'Lead workflow audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot conversion page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
