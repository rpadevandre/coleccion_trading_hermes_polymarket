export type RouteKey = 'landing' | 'roi' | 'demo' | 'audit' | 'pilot';

export type FrontendView = {
  key: RouteKey;
  navLabel: string;
  name: string;
  path: string;
  description: string;
  primaryOutcome: string;
  ctaLabel: string;
};

export const businessMeta = {
  name: 'HVAC Missed-Call Recovery',
  shortName: 'HVAC Call Recovery',
  headline: 'Turn every missed HVAC call into a reviewed dispatch opportunity.',
  subheadline:
    'AI-assisted intake, urgency triage, owner alerts and audit-ready follow-up for small HVAC operators who lose revenue after hours.',
  accent: '#f97316',
  accentDark: '#9a3412',
  marketProof: 'Built for owner-led HVAC teams with 2–25 technicians and no 24/7 dispatcher.',
  metric: '$8k–$40k/mo revenue leakage surfaced in a 30-day missed-call audit',
  buyerPromise:
    'In one week we show how many missed calls were emergencies, quotes or maintenance renewals — then route recoverable jobs to a human before automation touches customers.',
  riskCopy:
    'No robocalling, no autonomous customer commitments and no real customer data required for this prototype. Every suggested reply stays human-reviewed.',
  validationQuestions: [
    'How many calls go to voicemail after 5pm or during peak season?',
    'Which missed calls become emergency replacement, repair or maintenance-plan revenue?',
    'Who should review urgent captures before a tech or customer gets notified?'
  ],
  proofPoints: [
    'After-hours intake script tailored to HVAC emergencies, quotes and maintenance plans.',
    'Dispatcher confidence flags for low-confidence transcripts or incomplete addresses.',
    'Recovered-revenue dashboard that separates booked jobs from soft follow-up leads.'
  ],
  sampleCalls: [
    {
      caller: 'Mrs. Alvarez',
      issue: 'AC stopped cooling, elderly parent in home',
      urgency: 'Emergency',
      route: 'Owner + on-call tech',
      value: '$850 repair / $9,500 replacement risk'
    },
    {
      caller: 'Lakeview HOA',
      issue: 'Three-unit maintenance quote request',
      urgency: 'Quote follow-up',
      route: 'Estimator queue',
      value: '$3,200 proposal opportunity'
    },
    {
      caller: 'Existing plan customer',
      issue: 'Voicemail about annual tune-up renewal',
      urgency: 'Retention',
      route: 'CSR next business morning',
      value: '$219 plan renewal'
    }
  ]
} as const;

export const frontendViews: FrontendView[] = [
  {
    key: 'landing',
    navLabel: 'Problem',
    name: 'Missed-call recovery landing',
    path: '/landing',
    description: 'Buyer-validation landing page for HVAC owners who suspect voicemail is leaking urgent jobs.',
    primaryOutcome: 'Move owners into the ROI calculator or free missed-call audit request.',
    ctaLabel: 'Estimate missed revenue'
  },
  {
    key: 'roi',
    navLabel: 'ROI',
    name: 'Missed-call ROI calculator',
    path: '/roi-calculator',
    description: 'Interactive estimator for weekly missed calls, average job value and realistic recovery rate.',
    primaryOutcome: 'Quantify a dollar leakage range before asking for buyer contact details.',
    ctaLabel: 'Review my audit fit'
  },
  {
    key: 'demo',
    navLabel: 'Demo flow',
    name: 'Call-to-dispatch demo',
    path: '/demo-call-flow',
    description: 'Visual walkthrough of transcript capture, urgency classification, human review and dispatch routing.',
    primaryOutcome: 'Show the concierge workflow without implying production integrations or autonomous actions.',
    ctaLabel: 'Request audit worksheet'
  },
  {
    key: 'audit',
    navLabel: 'Free audit',
    name: 'Free missed-call audit form',
    path: '/free-audit-form',
    description: 'Lead-capture form focused on call volume, seasonality, after-hours process and human reviewer fit.',
    primaryOutcome: 'Collect enough non-sensitive operational detail to qualify a manual pilot.',
    ctaLabel: 'Submit audit request'
  },
  {
    key: 'pilot',
    navLabel: 'Pilot',
    name: 'Qualified pilot signup',
    path: '/pilot-signup',
    description: 'Conversion page for HVAC companies ready to test a 30-day concierge recovery workflow.',
    primaryOutcome: 'Confirm pilot readiness, buyer authority and success metrics before any build/deploy work.',
    ctaLabel: 'Reserve pilot review'
  }
];
