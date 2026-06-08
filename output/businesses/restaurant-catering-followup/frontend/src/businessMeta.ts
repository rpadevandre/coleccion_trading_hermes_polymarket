export const businessMeta = {
    name: 'Restaurant Catering Follow-Up Copilot',
    headline: 'Stop catering inquiries from dying in the inbox.',
    subheadline: 'Capture event details, reminders and quote checklists for restaurants selling catering.',
    accent: '#dc2626',
    metric: 'Catering revenue recovered from faster follow-up',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for restaurants.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'EventInquiryDemo', path: '/event-inquiry-demo', description: 'Demo inquiry parsing.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'CateringRevenueCalculator', path: '/catering-revenue-calculator', description: 'Calculator for lost catering value.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'InboxAuditForm', path: '/inbox-audit-form', description: 'Inbox workflow audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot signup page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
