# Layer Progress — HVAC Missed-Call Recovery

    ## Frontend

    - Landing: Public page explaining lost revenue from missed HVAC calls and after-hours voicemail.
- ROICalculator: Estimate missed-call revenue leak from average ticket size, missed calls/week and close rate.
- DemoCallFlow: Visual walkthrough of after-hours call capture, triage and dispatch notification.
- FreeAuditForm: Collect company size, service area, call volume and current after-hours process.
- PilotSignup: Convert qualified operators into a manual/concierge pilot.

    ## Backend motor

    - CallIntakeService: Accept call transcript/manual entry, normalize caller/job/location/urgency fields.
- UrgencyClassifier: Classify emergency, next-day, maintenance, quote request, spam or needs-human-review.
- DispatchRouter: Route urgent jobs to owner/tech notification queues based on service area and rules.
- RevenueEstimator: Estimate saved/lost revenue and produce weekly recovery metrics.
- AuditLogService: Record every classification, human edit, notification and status transition.

    ## Admin panel

    - OpsDashboard: KPIs: missed calls captured, urgent jobs, recovered revenue, response time.
- CallQueue: Review all inbound call items with AI classification and confidence.
- CallDetail: Transcript, extracted fields, dispatch decision, edit history and notes.
- RoutingRules: Configure service areas, emergency categories and notification recipients.
- Analytics: Weekly recovery trends, lead source breakdown and missed opportunity value.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
