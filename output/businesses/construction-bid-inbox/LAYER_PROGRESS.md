# Layer Progress — Construction Bid Inbox

    ## Frontend

    - Landing: Public page for turning chaotic bid requests into a clean bid pipeline.
- BidInboxDemo: Show an email/RFP transformed into structured scope and checklist.
- PipelineCalculator: Estimate admin hours saved and bid throughput increase.
- TradeFitForm: Collect trade, region, project size and current estimating workflow.
- PilotSignup: Invite contractors to a manual bid-inbox cleanup pilot.

    ## Backend motor

    - BidIntakeService: Ingest emails/manual bid requests and attachments metadata.
- ScopeExtractor: Extract trade, location, due date, scope, exclusions and missing files.
- BidFitScorer: Score fit based on geography, size, trade, deadline and risk.
- ChecklistGenerator: Generate estimator-ready missing-info/checklist notes.
- PipelineStatusService: Track new/reviewing/bid/no-bid/submitted/lost/won states.

    ## Admin panel

    - BidDashboard: Pipeline counts, due dates, potential value and bottlenecks.
- BidQueue: Prioritized bid inbox with fit score and deadline.
- BidDetail: Scope summary, missing docs, risks and estimator notes.
- NoBidRules: Configure bad-fit criteria and trade/geography limits.
- EstimatorAnalytics: Bid velocity, win/loss notes and opportunity value.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
