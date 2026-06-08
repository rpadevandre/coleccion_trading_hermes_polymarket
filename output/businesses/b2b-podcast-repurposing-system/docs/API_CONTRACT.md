# API Contract — B2B Podcast Repurposing System

Base path: `/api/v1`

All endpoints require workspace-scoped authentication unless explicitly marked public. Responses are JSON. File/media uploads use pre-signed upload URLs in the recommended implementation.

## Public lead endpoints

### `POST /leads/sample-pack-request`
Creates a marketing lead from the public site.

Request:
```json
{
  "name": "Jane Marketer",
  "email": "jane@example.com",
  "company": "Example SaaS",
  "website": "https://example.com",
  "podcast_url": "https://example.com/podcast",
  "episodes_per_month": 4,
  "primary_goal": "more LinkedIn and sales enablement content",
  "consent_to_contact": true
}
```

Response `201`:
```json
{ "lead_id": "lead_123", "status": "received" }
```

## Workspace endpoints

### `GET /workspaces/{workspace_id}/dashboard`
Returns activity metrics and next actions.

Response:
```json
{
  "episodes": { "total": 12, "in_review": 3, "failed": 0 },
  "assets": { "drafted": 240, "approved": 117, "exported": 90 },
  "next_actions": ["Review 18 LinkedIn drafts", "Export June founder POV pack"]
}
```

### `POST /workspaces/{workspace_id}/episodes`
Creates an episode ingest job.

Request:
```json
{
  "source_type": "youtube",
  "source_url": "https://youtube.com/watch?v=...",
  "title": "How CFOs evaluate security spend",
  "guest_name": "Alex CFO",
  "guest_company": "ExampleCo",
  "campaign_id": "camp_123",
  "consent_status": "confirmed",
  "target_audience": "B2B SaaS CFOs"
}
```

Response `202`:
```json
{ "episode_id": "ep_123", "status": "ingesting", "job_id": "job_123" }
```

### `GET /workspaces/{workspace_id}/episodes/{episode_id}`
Returns episode metadata, job status, transcript summary, moments, and draft counts.

### `POST /workspaces/{workspace_id}/episodes/{episode_id}/regenerate`
Regenerates selected asset types from current transcript/moments.

Request:
```json
{
  "asset_types": ["linkedin_post", "sales_snippet"],
  "moment_ids": ["mom_123", "mom_456"],
  "instructions": "Make hooks more tactical and reduce hype."
}
```

## Asset endpoints

### `GET /workspaces/{workspace_id}/assets`
Query params: `status`, `episode_id`, `asset_type`, `campaign_id`, `assigned_to`, `limit`, `cursor`.

### `PATCH /workspaces/{workspace_id}/assets/{asset_id}`
Updates draft body, CTA, status, tags, or reviewer assignment.

Request:
```json
{
  "body_markdown": "Updated post...",
  "status": "approved",
  "review_note": "Quote verified against timestamp."
}
```

### `POST /workspaces/{workspace_id}/assets/{asset_id}/comments`
Adds review comment.

### `POST /workspaces/{workspace_id}/exports`
Creates export package from approved assets.

Request:
```json
{
  "asset_ids": ["asset_1", "asset_2"],
  "format": "markdown",
  "include_source_timestamps": true
}
```

Response:
```json
{ "export_id": "export_123", "download_url": "https://signed-url.example" }
```

## Admin endpoints

### `GET /admin/jobs`
Internal-only job queue with filters by status and failure type.

### `POST /admin/jobs/{job_id}/retry`
Retries failed ingest/transcript/drafting job.

### `GET /admin/workspaces/{workspace_id}/audit-events`
Returns audit events for support/security review.

## Error format

```json
{
  "error": {
    "code": "LOW_TRANSCRIPT_CONFIDENCE",
    "message": "Transcript confidence below workspace threshold; human review required.",
    "request_id": "req_123"
  }
}
```
