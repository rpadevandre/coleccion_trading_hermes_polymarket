# Layer Progress — Chiropractic Patient Reactivation Engine

    ## Frontend

    - Landing: Public page for reactivating inactive patients without spam.
- RecoveryCalculator: Estimate recovered appointments from inactive patient list.
- CampaignPreview: Show patient segment and human-approved message flow.
- InactiveListAuditForm: Collect list size, visit recency and campaign history.
- PilotSignup: Request a limited reactivation pilot.

    ## Backend motor

    - PatientListImportService: Import sanitized inactive-patient CSV and validate fields.
- ReactivationSegmenter: Segment by recency, visit type, last status and consent/eligibility.
- MessageDraftService: Draft gentle rebooking/nurture messages for staff approval.
- OptOutSuppressionService: Track opt-outs and suppress future contact.
- RecoveredAppointmentTracker: Track replies, booked appointments and recovery metrics.

    ## Admin panel

    - ReactivationDashboard: Segments, scheduled messages, replies and recovered appointments.
- SegmentBuilder: Build and review inactive patient cohorts.
- CampaignApproval: Review/edit/approve message drafts before sending.
- ReplyInbox: Track patient replies, booked, no response, opt-out.
- ComplianceLog: Data import, consent, opt-out and approval audit events.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
