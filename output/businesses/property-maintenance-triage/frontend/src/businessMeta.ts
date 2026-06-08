export const businessMeta = {
    name: 'Property Maintenance Triage',
    headline: 'Turn tenant maintenance chaos into prioritized work orders.',
    subheadline: 'AI triage for property managers handling requests across texts, email and forms.',
    accent: '#059669',
    metric: 'Hours saved per manager per week',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation landing page for property managers.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'TenantRequestDemo', path: '/tenant-request-demo', description: 'Demo request intake and triage result.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ROICalculator', path: '/r-o-i-calculator', description: 'Calculator for manager time saved and emergency leakage.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PortfolioAuditForm', path: '/portfolio-audit-form', description: 'Audit form for unit count and workflow pain.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot booking page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
