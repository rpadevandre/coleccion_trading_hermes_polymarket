# Layer Progress — MSP Security Reporting Copilot

    ## Frontend

    - Landing: Public page for MSPs turning security work into client-ready reports.
- ReportBeforeAfter: Show raw security noise vs executive summary/report.
- ClientProofDemo: Demonstrate monthly client report generation and approval flow.
- StackAuditForm: Collect tools used, number of clients and reporting pain.
- PilotSignup: Invite MSPs to test on one anonymized client report.

    ## Backend motor

    - EvidenceImportService: Import CSV/manual evidence from security tools and ticket systems.
- SignalNormalizer: Normalize findings, alerts, tickets and remediation evidence.
- RiskNarrativeWriter: Draft executive-friendly summary with technical appendix.
- ClientReportGenerator: Assemble report sections, metrics, risks and next actions.
- ApprovalAuditService: Track edits, approvals, exports and client delivery status.

    ## Admin panel

    - ClientDashboard: Client accounts, report status, risk trends and pending approvals.
- EvidenceQueue: Imported findings needing mapping or review.
- ReportBuilder: Editable report sections with AI suggestions and source links.
- TemplateSettings: Configure report templates, tone and risk language.
- DeliveryAudit: Export/delivery history and approval trace.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
