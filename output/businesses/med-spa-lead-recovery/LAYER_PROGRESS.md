# Layer Progress — Med Spa Lead Recovery

    ## Frontend

    - Landing: Public page for missed med-spa leads and consult booking leakage.
- LeadLeakCalculator: Estimate lost consult value from slow replies and missed DMs/calls.
- InstagramDMFlow: Demo DM/form/call captured into a consult follow-up queue.
- FreeLeadAuditForm: Collect services offered, lead sources and booking process.
- PilotSignup: Convert interested clinics into a follow-up pilot.

    ## Backend motor

    - LeadIntakeService: Ingest web forms, missed calls, SMS and manual DM exports.
- TreatmentIntentClassifier: Classify treatment interest, budget/timing and consult readiness.
- FollowupDraftService: Draft compliant consult booking messages for human approval.
- ComplianceLanguageGuard: Flag medical claims, guarantees and risky before/after wording.
- ConsultRevenueTracker: Track booked consults, no-shows and estimated recovered revenue.

    ## Admin panel

    - LeadDashboard: New leads, hot consults, booked consults and recovered value.
- LeadQueue: Prioritized follow-up queue by source and intent.
- LeadDetail: Contact data, service interest, notes, drafts and history.
- TreatmentSettings: Services, disclaimers, approved templates and routing rules.
- RevenueAnalytics: Lead source performance, booking rate and lost/recovered value.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
