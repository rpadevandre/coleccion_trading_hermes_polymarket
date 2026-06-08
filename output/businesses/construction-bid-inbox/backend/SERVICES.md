# Backend Services

- `BidIntakeService` — Ingest emails/manual bid requests and attachments metadata.
- `ScopeExtractor` — Extract trade, location, due date, scope, exclusions and missing files.
- `BidFitScorer` — Score fit based on geography, size, trade, deadline and risk.
- `ChecklistGenerator` — Generate estimator-ready missing-info/checklist notes.
- `PipelineStatusService` — Track new/reviewing/bid/no-bid/submitted/lost/won states.
