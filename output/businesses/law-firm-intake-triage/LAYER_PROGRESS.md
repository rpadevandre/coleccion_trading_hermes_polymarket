# Layer Progress — Law Firm Intake Triage

    ## Frontend

    - Landing: Public page for attorney-ready intake summaries and after-hours capture.
- PracticeAreaDemo: Show inquiry categorized into practice area and intake checklist.
- IntakeQualityCalculator: Estimate staff/attorney time lost on low-quality intake.
- FirmAuditForm: Collect practice areas, inquiry volume and current intake flow.
- PilotSignup: Invite a firm to test on non-confidential/sample inquiries first.

    ## Backend motor

    - LegalInquiryIntakeService: Capture structured inquiry with disclaimers and consent.
- PracticeAreaClassifier: Categorize practice area, urgency and missing facts.
- AttorneySummaryWriter: Create factual attorney-ready summaries without legal advice.
- ConflictChecklistService: Flag conflict-check fields and jurisdiction questions.
- IntakeAuditService: Log access, edits, routing decisions and disclaimers accepted.

    ## Admin panel

    - IntakeDashboard: New inquiries, urgent matters, practice area mix and response times.
- InquiryQueue: Prioritized intake queue with fit/urgency indicators.
- InquiryDetail: Facts, summary, missing info, disclaimers and routing decision.
- PracticeRules: Practice areas, routing rules, rejected categories and disclaimers.
- ComplianceAudit: Access logs, summary edits and human review decisions.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
