# Frontend Views — B2B Podcast Repurposing System

## Public marketing site

### 1. Home
- Hero: "Turn one B2B podcast episode into a week of sales-ready content."
- Subhero: for founder-led and lean B2B marketing teams with unused long-form interviews.
- CTA: "Upload an episode for a sample content pack" / "Book a 15-minute content audit".
- Proof strip: episode-to-assets workflow, 48-hour review promise, human approval.
- Problem section: great interviews vanish after publishing; teams lack time to mine them.
- Offer section: episode content pack, monthly repurposing engine, sales enablement add-on.
- Validation CTA: paid pilot deposit or sample pack request.

### 2. Sample Pack Page
- Shows anonymized example assets from a mock episode:
  - 5 LinkedIn post types.
  - 3 clip briefs with timestamps.
  - 1 newsletter block.
  - 1 blog outline.
  - 3 sales snippets.
- Includes clear note: sample content is illustrative and not based on customer data.

### 3. Pricing / Pilot
- Pilot: $500-$1,500 for 2-4 episodes depending on review depth.
- Monthly: $1,500-$4,000 for recurring teams.
- Upsell: editor QA, short-form video editing coordination, CMS uploads.
- Money-focused guarantee language: "If we cannot identify at least 20 usable content assets from two episodes, we refund the pilot fee."

### 4. Lead Capture
- Fields: name, work email, company, website, podcast URL, episodes/month, primary goal, consent checkbox.
- Optional upload/link for one episode.
- Confirmation: explains that no content is published automatically.

## Authenticated customer app

### 1. Workspace Dashboard
- Metrics: episodes ingested, assets drafted, assets approved, review backlog, average review time.
- "Next best action": upload episode, review drafts, export approved pack.
- Campaign filter: founder POV, product education, customer stories, event follow-up.

### 2. Episode Intake
- Source selector: YouTube/RSS/file/transcript/manual notes.
- Episode metadata: title, guest, company, topic, publish date, target audience, campaign.
- Voice profile selector and compliance notes.
- Consent checkbox for using transcript/media.

### 3. Episode Detail
- Status timeline: ingested -> transcribed -> moments extracted -> drafts generated -> in review -> exported.
- Transcript viewer with speaker labels and timestamps.
- Highlighted moments with AI score and editor notes.
- Regenerate selected asset from a specific timestamp.

### 4. Asset Review Board
- Kanban columns: Draft, Needs edits, Approved, Exported, Archived.
- Card data: asset type, channel, hook, source timestamp, risk flags, last editor.
- Bulk actions: approve, assign, export, archive.

### 5. Asset Editor
- Split layout: source quote/transcript on left, draft asset on right.
- Controls: voice tone, CTA, length, format, "make more tactical", "reduce hype".
- Required checks: quote accuracy, claim safety, guest/company spelling, CTA fit.
- Version history and comments.

### 6. Export Center
- Select campaign and asset types.
- Export formats: Markdown pack, CSV for scheduler, Google Docs copy block, Notion blocks.
- Include usage notes for sales team.

### 7. Settings
- Brand voice, glossary, forbidden phrases, competitor names, default CTAs.
- User roles, retention policy, integrations placeholders.

## Responsive behavior

- Mobile: review board becomes stacked list; asset editor supports quick approve/comment.
- Desktop: optimized for side-by-side transcript and asset editing.
