# Layer Progress — Property Maintenance Triage

    ## Frontend

    - Landing: Public page for reducing chaotic tenant maintenance messages.
- TenantRequestDemo: Show tenant issue submission and AI triage result.
- ROICalculator: Estimate manager time saved and emergency leakage reduction.
- PortfolioAuditForm: Collect unit count, channels used, issue volume and vendor process.
- PilotSignup: Book a workflow audit for a property manager.

    ## Backend motor

    - RequestIntakeService: Ingest tenant maintenance requests from form/email/manual entry.
- IssueClassifier: Classify plumbing/electrical/HVAC/appliance/general and emergency level.
- VendorRoutingEngine: Suggest vendor/category/routing path and next required info.
- TenantSummaryWriter: Produce manager/vendor-ready summaries without overpromising repair actions.
- SLAWatcher: Track status, response deadlines, escalations and unresolved items.

    ## Admin panel

    - PortfolioDashboard: Open issues, emergencies, aging tickets and vendor workload.
- RequestQueue: Triage queue with category, urgency and missing info.
- RequestDetail: Tenant message, extracted facts, suggested route and audit log.
- VendorSettings: Vendors by trade, coverage, availability and contact rules.
- SLAAnalytics: Resolution time, emergency rate and repeated-property issues.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
