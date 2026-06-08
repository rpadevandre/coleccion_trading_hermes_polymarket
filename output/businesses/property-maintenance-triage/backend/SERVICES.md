# Backend Services

- `RequestIntakeService` — Ingest tenant maintenance requests from form/email/manual entry.
- `IssueClassifier` — Classify plumbing/electrical/HVAC/appliance/general and emergency level.
- `VendorRoutingEngine` — Suggest vendor/category/routing path and next required info.
- `TenantSummaryWriter` — Produce manager/vendor-ready summaries without overpromising repair actions.
- `SLAWatcher` — Track status, response deadlines, escalations and unresolved items.
