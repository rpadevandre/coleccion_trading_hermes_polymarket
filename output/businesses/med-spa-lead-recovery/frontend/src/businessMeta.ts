export type RouteKey =
  | 'landing'
  | 'lead-leak-calculator'
  | 'instagram-dm-flow'
  | 'free-lead-audit-form'
  | 'pilot-signup';

export type FrontendView = {
  name: string;
  route: RouteKey;
  path: string;
  navLabel: string;
  description: string;
  primaryOutcome: string;
  buyerSignal: string;
};

export const businessMeta = {
  name: 'Med Spa Lead Recovery',
  shortName: 'Lead Recovery',
  headline: 'Recover med-spa consult leads before they book somewhere else.',
  subheadline:
    'A human-approved follow-up workspace for aesthetic clinics that lose Botox, filler, laser and body-contouring consults to slow replies across Instagram, forms, SMS and missed calls.',
  accent: '#db2777',
  accentDark: '#9d174d',
  metric: 'Booked consults recovered from slow replies',
  targetBuyer: 'Owner-operators, practice managers and patient coordinators at cash-pay med spas',
  validationPromise:
    'Validate willingness to pay by showing the dollar value of unworked leads and asking for a low-risk 14-day recovery pilot.',
  complianceNote:
    'No medical advice, treatment guarantees, before/after promises or automated patient-facing messages. Every draft stays human-reviewed before outreach.',
  primaryCta: 'Run my free lead leak audit',
  secondaryCta: 'Preview the DM recovery flow',
} as const;

export const leadSources = ['Instagram DMs', 'Website forms', 'Missed calls', 'SMS replies', 'Meta lead ads'] as const;

export const treatmentLines = [
  { name: 'Injectables', value: 475, examples: 'Botox, Dysport, filler consults' },
  { name: 'Laser / skin', value: 900, examples: 'Laser hair removal, resurfacing, IPL' },
  { name: 'Body contouring', value: 1800, examples: 'CoolSculpting, Emsculpt, RF' },
  { name: 'Membership / packages', value: 1250, examples: 'Facial memberships, treatment bundles' },
] as const;

export const proofPoints = [
  'Highlights hot leads that waited more than 15 minutes for a reply.',
  'Shows estimated consult value before asking for a sales call.',
  'Drafts compliant follow-up language for staff approval instead of auto-sending.',
  'Captures buyer proof: lead sources, average treatment value, booking bottleneck and pilot intent.',
] as const;

export const sampleLeads = [
  {
    source: 'Instagram DM',
    intent: 'Lip filler pricing + first available appointment',
    age: '2h 14m old',
    value: '$650 est.',
    risk: 'High',
    draft: 'Thanks for reaching out — we can help you compare options in a consult. Would you like our coordinator to send the next two available times?',
  },
  {
    source: 'Website form',
    intent: 'Laser hair removal package',
    age: '48m old',
    value: '$1,100 est.',
    risk: 'Medium',
    draft: 'We received your laser hair removal request. A coordinator can answer pricing and timing questions after confirming the treatment area.',
  },
  {
    source: 'Missed call',
    intent: 'Botox appointment before event',
    age: '19m old',
    value: '$425 est.',
    risk: 'High',
    draft: 'Sorry we missed you. If you are still looking for appointment options, reply here and our team will help coordinate availability.',
  },
] as const;

export const frontendViews: FrontendView[] = [
  {
    name: 'Landing',
    route: 'landing',
    path: '/landing',
    navLabel: 'Overview',
    description: 'Public validation page for med spas losing consult-ready leads across DMs, forms and phone calls.',
    primaryOutcome: 'Move a qualified med spa owner or manager into the free lead leak audit.',
    buyerSignal: 'Clicks audit CTA or asks to preview how staff approve follow-up drafts.',
  },
  {
    name: 'LeadLeakCalculator',
    route: 'lead-leak-calculator',
    path: '/lead-leak-calculator',
    navLabel: 'Calculator',
    description: 'Estimate monthly consult revenue at risk from slow response times and unworked lead sources.',
    primaryOutcome: 'Quantify the pain in dollars before the pilot ask.',
    buyerSignal: 'Inputs real missed lead volume and selects a recovery target.',
  },
  {
    name: 'InstagramDMFlow',
    route: 'instagram-dm-flow',
    path: '/instagram-dm-flow',
    navLabel: 'DM Flow',
    description: 'Demonstrate how an Instagram DM, form or missed call becomes a reviewed consult follow-up task.',
    primaryOutcome: 'Make the product workflow tangible without using real patient data.',
    buyerSignal: 'Reviews sample leads and accepts the human-approval workflow.',
  },
  {
    name: 'FreeLeadAuditForm',
    route: 'free-lead-audit-form',
    path: '/free-lead-audit-form',
    navLabel: 'Audit Form',
    description: 'Collect non-sensitive clinic workflow details needed to score lead leakage and pilot fit.',
    primaryOutcome: 'Capture qualified audit requests with clear no-PHI guardrails.',
    buyerSignal: 'Submits lead sources, treatment focus, response SLA and booking bottleneck.',
  },
  {
    name: 'PilotSignup',
    route: 'pilot-signup',
    path: '/pilot-signup',
    navLabel: 'Pilot',
    description: 'Convert interested clinics into a small, measurable 14-day lead recovery pilot.',
    primaryOutcome: 'Secure pilot commitment from clinics with enough missed-lead volume.',
    buyerSignal: 'Chooses a start window, success metric and approval owner.',
  },
];

export function getView(route: RouteKey) {
  return frontendViews.find((view) => view.route === route) ?? frontendViews[0];
}
