export type RouteKey = 'landing' | 'report-before-after' | 'client-proof-demo' | 'stack-audit-form' | 'pilot-signup';

export type FrontendView = {
  key: RouteKey;
  name: string;
  navLabel: string;
  path: string;
  description: string;
  primaryOutcome: string;
};

export const businessMeta = {
  name: 'MSP Security Reporting Copilot',
  shortName: 'Security Reporting Copilot',
  headline: 'Turn quiet MSP security work into client-ready proof-of-value reports.',
  subheadline:
    'A validation prototype for MSP owners who need monthly security reporting that explains what was protected, what improved and what needs client approval next.',
  accent: '#6d28d9',
  darkAccent: '#312e81',
  metric: 'Cut a 4–6 hour monthly reporting chore into a 20-minute approval workflow',
  buyer: 'MSP owners, vCISOs and account managers serving 20–250 seat SMB clients',
  promise: 'Import anonymized security/ticket evidence, draft executive language and keep a human approval trail before anything reaches a client.',
  guardrails: [
    'Prototype uses anonymized sample evidence only — no tenant secrets, credentials, client names or real customer data.',
    'Every AI-written paragraph requires MSP review and approval before client export.',
    'Reports cite source evidence so account managers can defend each claim in a QBR.',
  ],
  proofPoints: [
    'Show security activity clients usually never see: blocked threats, patched systems, MFA cleanup and backup checks.',
    'Translate technical tool noise into owner-friendly risk, action and business-impact language.',
    'Create a repeatable report process without forcing the MSP to replace its PSA, RMM, EDR or documentation stack.',
  ],
  stackOptions: ['PSA tickets', 'RMM alerts', 'EDR findings', 'M365 secure score', 'Backup reports', 'Vulnerability scans'],
} as const;

export const frontendViews: FrontendView[] = [
  {
    key: 'landing',
    name: 'Landing',
    navLabel: 'Overview',
    path: '/landing',
    description: 'Public validation page for MSPs who need better client-facing security proof.',
    primaryOutcome: 'Qualify MSPs by stack, report frequency, client count and willingness to test with anonymized evidence.',
  },
  {
    key: 'report-before-after',
    name: 'ReportBeforeAfter',
    navLabel: 'Before / After',
    path: '/report-before-after',
    description: 'Contrast raw technical alert noise with a clear executive-ready monthly security narrative.',
    primaryOutcome: 'Make the value obvious enough that an MSP wants a sample report from their own anonymized evidence.',
  },
  {
    key: 'client-proof-demo',
    name: 'ClientProofDemo',
    navLabel: 'Approval Demo',
    path: '/client-proof-demo',
    description: 'Interactive demo of evidence review, AI draft, human approval and delivery readiness.',
    primaryOutcome: 'Validate whether MSPs trust a human-in-the-loop copilot for report generation.',
  },
  {
    key: 'stack-audit-form',
    name: 'StackAuditForm',
    navLabel: 'Stack Audit',
    path: '/stack-audit-form',
    description: 'Tool stack and reporting-pain intake for a no-secrets security report workflow audit.',
    primaryOutcome: 'Capture structured buyer signal without collecting sensitive security data.',
  },
  {
    key: 'pilot-signup',
    name: 'PilotSignup',
    navLabel: 'Pilot',
    path: '/pilot-signup',
    description: 'Pilot signup for one anonymized client report and a guided approval workflow.',
    primaryOutcome: 'Convert qualified MSPs into a narrow pilot with one client, one month and one approved report.',
  },
];

export const sampleEvidence = [
  {
    tool: 'EDR',
    source: 'Endpoint alert summary',
    raw: '21 detections quarantined; 4 false positives closed; 2 devices need agent update.',
    executive: 'Threat protection blocked suspicious activity across 21 events. Two laptops still need agent updates to keep coverage complete.',
    status: 'Needs owner-friendly wording',
  },
  {
    tool: 'M365',
    source: 'Secure score change',
    raw: 'Score +7%; legacy auth disabled; 3 shared mailboxes excluded pending approval.',
    executive: 'Microsoft 365 posture improved after legacy sign-in controls were tightened. Three mailbox exceptions need client approval.',
    status: 'Ready for review',
  },
  {
    tool: 'Backup',
    source: 'Backup verification report',
    raw: '29/30 backup jobs passed; FILE-02 failed twice then passed manual retry.',
    executive: 'Backup coverage was healthy this month. One server needed manual remediation and is now passing verification.',
    status: 'Source attached',
  },
];

export const reportSections = [
  'Executive summary',
  'Protected activity this month',
  'Open risks requiring approval',
  'Completed remediation proof',
  'Next-month recommendations',
];

export const qualificationSignals = [
  'Serves at least 15 managed clients',
  'Currently spends 2+ hours per client per month on reporting or QBR prep',
  'Can provide anonymized exports/screenshots from current tools',
  'Has a human approver for any client-facing security language',
];
