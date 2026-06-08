export const businessMeta = {
    name: 'Chiropractic Reactivation Engine',
    headline: 'Reactivate inactive patients with gentle, approved campaigns.',
    subheadline: 'Segment inactive patient lists, draft messages and track recovered appointments.',
    accent: '#16a34a',
    metric: 'Recovered appointments from existing patient lists',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for chiropractic clinics.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'RecoveryCalculator', path: '/recovery-calculator', description: 'Calculator for recovered appointments.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'CampaignPreview', path: '/campaign-preview', description: 'Demo segment and message preview.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'InactiveListAuditForm', path: '/inactive-list-audit-form', description: 'Inactive list audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot signup page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
