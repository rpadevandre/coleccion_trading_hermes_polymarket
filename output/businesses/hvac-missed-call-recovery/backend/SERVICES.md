# Backend Services

- `CallIntakeService` — Accept call transcript/manual entry, normalize caller/job/location/urgency fields.
- `UrgencyClassifier` — Classify emergency, next-day, maintenance, quote request, spam or needs-human-review.
- `DispatchRouter` — Route urgent jobs to owner/tech notification queues based on service area and rules.
- `RevenueEstimator` — Estimate saved/lost revenue and produce weekly recovery metrics.
- `AuditLogService` — Record every classification, human edit, notification and status transition.
