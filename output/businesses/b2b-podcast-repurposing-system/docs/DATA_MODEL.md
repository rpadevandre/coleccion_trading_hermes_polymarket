# Data Model — B2B Podcast Repurposing System

## Entities

### Workspace
- `id`
- `name`
- `website`
- `market_segment`
- `plan_type`: sample, pilot, monthly, paused
- `default_language`: en, es, other
- `retention_policy_days`
- `created_at`, `updated_at`

### User
- `id`
- `workspace_id`
- `email`
- `name`
- `role`: owner, marketer, editor, viewer, internal_operator
- `mfa_enabled`
- `last_login_at`

### BrandProfile
- `id`
- `workspace_id`
- `voice_description`
- `approved_terms[]`
- `forbidden_terms[]`
- `competitor_names[]`
- `default_ctas[]`
- `claim_rules`
- `example_posts[]`

### Episode
- `id`
- `workspace_id`
- `title`
- `source_type`: youtube, rss, file, transcript, manual
- `source_url`
- `media_storage_key`
- `guest_name`
- `guest_company`
- `host_name`
- `campaign_id`
- `consent_status`: confirmed, missing, not_required, exception
- `status`: ingesting, transcribing, extracting, drafting, review, exported, failed
- `published_at`
- `created_at`, `updated_at`

### Transcript
- `id`
- `episode_id`
- `language`
- `speaker_map`
- `text_storage_key`
- `confidence_score`
- `low_confidence_segments[]`
- `created_at`

### Moment
- `id`
- `episode_id`
- `start_time`
- `end_time`
- `speaker`
- `quote`
- `summary`
- `moment_type`: pain, framework, proof, story, objection, contrarian, tactic
- `business_value_score`
- `risk_score`
- `tags[]`

### AssetDraft
- `id`
- `episode_id`
- `moment_id`
- `asset_type`: linkedin_post, newsletter_block, blog_outline, clip_brief, sales_snippet, email_blurb
- `channel`
- `title`
- `body_markdown`
- `cta`
- `source_timestamp`
- `status`: draft, needs_edits, approved, exported, archived
- `risk_flags[]`
- `created_by`: ai, human
- `model_version`
- `created_at`, `updated_at`

### ReviewComment
- `id`
- `asset_draft_id`
- `user_id`
- `body`
- `resolution_status`: open, resolved
- `created_at`

### ExportPackage
- `id`
- `workspace_id`
- `campaign_id`
- `episode_ids[]`
- `asset_ids[]`
- `format`: markdown, csv, notion, gdoc_copy
- `storage_key`
- `created_by`
- `created_at`

### AuditEvent
- `id`
- `workspace_id`
- `actor_user_id`
- `event_type`
- `entity_type`
- `entity_id`
- `reason_code`
- `ip_address`
- `created_at`

## Relationships

- Workspace has many Users, Episodes, BrandProfiles, Campaigns.
- Episode has one Transcript and many Moments.
- Moment has many AssetDrafts.
- AssetDraft has many ReviewComments and versions.
- ExportPackage references approved AssetDrafts.
- AuditEvent records sensitive admin and customer actions.
