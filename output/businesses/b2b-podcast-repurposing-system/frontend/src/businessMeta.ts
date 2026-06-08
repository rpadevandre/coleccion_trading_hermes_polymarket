export const businessMeta = {
    name: 'B2B Podcast Repurposing System',
    headline: 'Turn one B2B conversation into a week of founder-led content.',
    subheadline: 'Extract insights, draft channel-native posts and queue content for approval.',
    accent: '#4f46e5',
    metric: 'One source conversation → multi-channel content queue',
  } as const;

  export const frontendViews = [
    { name: 'Landing', path: '/landing', description: 'Public validation page for founders/content teams.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'BeforeAfterDemo', path: '/before-after-demo', description: 'Demo transcript to content transformation.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'TranscriptUploadDemo', path: '/transcript-upload-demo', description: 'Transcript paste/upload demo.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'ContentCalendarPreview', path: '/content-calendar-preview', description: 'Calendar preview page.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
{ name: 'EpisodeAuditForm', path: '/episode-audit-form', description: 'Episode/source audit form.', primaryOutcome: 'Convert this page into validated pilot interest with measurable buyer signal.' },
  ] as const;
