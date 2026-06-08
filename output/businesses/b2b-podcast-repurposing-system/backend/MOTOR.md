# Backend Motor — B2B Podcast Repurposing System

## Purpose

Convert each long-form B2B podcast episode into a reviewed content package that a marketing or founder-led sales team can publish within 48 hours: LinkedIn posts, short clip briefs, newsletter blurbs, blog outlines, sales snippets, and guest follow-up assets.

## Core pipeline

1. **Ingest**
   - Accept YouTube URL, RSS episode URL, audio/video file, transcript file, or manual notes.
   - Store original media pointer, episode metadata, guest/company, host, topic tags, consent status, and target campaign.
2. **Transcribe + normalize**
   - Produce timestamped transcript.
   - Detect speaker turns, remove filler when used for written content, keep exact quotes for quote-card/clip use.
   - Mark transcript confidence and flag low-confidence words for human review.
3. **Strategic extraction**
   - Identify: strongest claims, customer pain points, contrarian takes, founder stories, proof points, case-study moments, tactical frameworks, and objection-handling snippets.
   - Score each moment for business value, novelty, clarity, and compliance risk.
4. **Asset generation**
   - Generate content drafts by channel:
     - LinkedIn text posts: founder voice, guest quote, tactical list, story post, debate prompt.
     - Newsletter section: 120-250 word episode takeaway.
     - Blog/SEO brief: title, H2s, search intent, excerpt, quotes.
     - Short clip brief: timestamp, hook, caption, B-roll note, CTA.
     - Sales enablement: "send this to prospects who ask about X" snippets.
   - Every output is labeled as draft, not auto-published.
5. **Editorial review**
   - Apply voice profile, forbidden claims, brand glossary, competitor exclusions, and channel formatting rules.
   - Route assets to reviewer queue with approve/request-change/reject states.
6. **Export**
   - Export Markdown, CSV, Google Doc-ready copy, Notion-ready blocks, CMS brief, or social scheduler CSV.
   - No direct publication in MVP unless explicitly enabled later.

## Key services

- `EpisodeIngestService`: validates sources, creates episode job, stores metadata.
- `TranscriptService`: transcript import/transcription, diarization, confidence flags.
- `InsightExtractionService`: extracts high-value moments and timestamps.
- `ContentDraftService`: creates channel-specific assets from approved moments.
- `VoiceGuardService`: checks tone, terminology, prohibited claims, and overpromising.
- `ReviewWorkflowService`: manages status, comments, editor assignments, and version history.
- `ExportService`: packages approved assets by workspace/campaign.
- `MetricsService`: tracks episode-to-asset yield, review cycle time, publish status, and attributed opportunities when manually entered.

## Data retention

- Raw media can be deleted after transcription if customer policy requires.
- Transcripts and generated assets are retained by workspace retention policy.
- Guest PII is limited to business contact metadata and should be editable/deletable by admins.

## Failure handling

- Ingest failures retry twice, then surface actionable errors.
- Low transcript confidence creates a review task instead of blocking all outputs.
- AI generation errors preserve job state and allow regeneration by asset type.
- Export failures never delete approved content.

## Pseudocode

```pseudo
on EpisodeSubmitted(source):
  episode = create_episode(source, status="ingesting")
  transcript = get_or_create_transcript(source)
  moments = extract_business_moments(transcript, workspace.strategy)
  drafts = []
  for moment in top_ranked(moments):
    drafts += generate_assets(moment, workspace.channel_rules)
  checked = apply_voice_and_claim_guards(drafts, workspace.brand_rules)
  create_review_queue(episode, checked)
  notify_editor(episode.ready_for_review_url)
```
