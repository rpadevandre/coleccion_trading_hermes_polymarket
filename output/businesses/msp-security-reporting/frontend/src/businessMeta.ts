export const businessMeta = {
    name: 'MSP Security Reporting Copilot',
    headline: 'Turn security work into client-ready reports MSPs can actually sell.',
    subheadline: 'Transform ticket/security evidence into executive summaries and monthly proof-of-value reports.',
    accent: '#7c3aed',
    metric: 'Monthly report production time cut dramatically',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for MSPs.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ReportBeforeAfter', path: '/report-before-after', description: 'Raw technical noise vs executive report.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ClientProofDemo', path: '/client-proof-demo', description: 'Demo client report approval flow.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'StackAuditForm', path: '/stack-audit-form', description: 'Tool stack and reporting pain intake.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot signup on anonymized report sample.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
