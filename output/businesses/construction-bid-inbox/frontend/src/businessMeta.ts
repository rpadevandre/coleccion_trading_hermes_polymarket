export const businessMeta = {
    name: 'Construction Bid Inbox',
    headline: 'Stop losing bid opportunities inside messy inboxes.',
    subheadline: 'Extract scope, due dates, fit scores and estimator checklists from bid requests.',
    accent: '#ea580c',
    metric: 'More bids reviewed without more admin work',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for contractors.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'BidInboxDemo', path: '/bid-inbox-demo', description: 'Demo bid request extraction.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PipelineCalculator', path: '/pipeline-calculator', description: 'Calculator for admin hours and bid throughput.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'TradeFitForm', path: '/trade-fit-form', description: 'Trade/geography fit intake form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'PilotSignup', path: '/pilot-signup', description: 'Pilot signup page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
