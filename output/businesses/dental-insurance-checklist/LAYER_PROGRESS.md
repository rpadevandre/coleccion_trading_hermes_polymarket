# Layer Progress — Dental Insurance Checklist

    ## Frontend

    - Landing: Public page around reducing insurance verification mistakes and rework.
- ChecklistDemo: Show a verification checklist generated from patient/procedure context.
- ReworkCalculator: Estimate admin time lost to missing insurance information.
- OfficeAuditForm: Collect office size, procedure mix and verification workflow.
- PilotSignup: Request a controlled checklist pilot.

    ## Backend motor

    - VerificationIntakeService: Capture patient/procedure/plan metadata without storing unnecessary PHI.
- ChecklistBuilder: Generate procedure-specific verification checklist and missing fields.
- PolicyLanguageSummarizer: Summarize plan notes into staff-readable reminders with source references.
- ComplianceGuard: Flag PHI/compliance-sensitive handling and avoid payment guarantees.
- VerificationAuditService: Track checklist completion, edits and verification status.

    ## Admin panel

    - VerificationDashboard: Pending verifications, completed checks and rework indicators.
- ChecklistQueue: Patients/procedures awaiting verification steps.
- ChecklistDetail: Checklist, source notes, completion state and staff comments.
- ProcedureTemplates: Configure checklist templates by procedure category.
- ComplianceLog: PHI access/change events and approval history.

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
