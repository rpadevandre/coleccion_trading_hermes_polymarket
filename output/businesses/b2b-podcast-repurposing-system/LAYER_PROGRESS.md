# Layer Progress — B2B Podcast Repurposing System

    ## Frontend

    - Landing: Public page for turning one B2B conversation into a week of content.
- BeforeAfterDemo: Show transcript fragment transformed into posts/thread/newsletter.
- TranscriptUploadDemo: Demo source upload/paste and output selection.
- ContentCalendarPreview: Show generated weekly publishing queue.
- EpisodeAuditForm: Collect audience, channel, tone and sample transcript.

    ## Backend motor

    - TranscriptIngestionService: Accept transcript text/notes and chunk into sections.
- InsightExtractor: Extract stories, claims, objections, frameworks and quotable moments.
- ChannelDraftGenerator: Generate LinkedIn, X, email and blog drafts by channel constraints.
- VoiceConsistencyScorer: Score drafts for founder voice, specificity and AI-generic language.
- PublishingQueueService: Create approval queue and calendar-ready content items.

    ## Admin panel

    - ContentDashboard: Sources, drafts, approvals and publishing queue.
- SourceLibrary: Transcripts/notes with extracted themes and status.
- DraftWorkspace: Edit drafts, regenerate sections and compare variants.
- VoiceSettings: Audience, tone, banned phrases, examples and CTA preferences.
- CalendarBoard: Scheduled/approved/published content by channel.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
