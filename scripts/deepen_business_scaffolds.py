from pathlib import Path
from textwrap import dedent

root = Path('/home/hermes/coleccion_trading_hermes_polymarket/output/businesses')

businesses = {
    'hvac-missed-call-recovery': {
        'name': 'HVAC Missed-Call Recovery',
        'domain': 'HVAC emergency/service companies',
        'frontend_pages': [
            ('Landing', 'Public page explaining lost revenue from missed HVAC calls and after-hours voicemail.'),
            ('ROICalculator', 'Estimate missed-call revenue leak from average ticket size, missed calls/week and close rate.'),
            ('DemoCallFlow', 'Visual walkthrough of after-hours call capture, triage and dispatch notification.'),
            ('FreeAuditForm', 'Collect company size, service area, call volume and current after-hours process.'),
            ('PilotSignup', 'Convert qualified operators into a manual/concierge pilot.'),
        ],
        'backend_modules': [
            ('CallIntakeService', 'Accept call transcript/manual entry, normalize caller/job/location/urgency fields.'),
            ('UrgencyClassifier', 'Classify emergency, next-day, maintenance, quote request, spam or needs-human-review.'),
            ('DispatchRouter', 'Route urgent jobs to owner/tech notification queues based on service area and rules.'),
            ('RevenueEstimator', 'Estimate saved/lost revenue and produce weekly recovery metrics.'),
            ('AuditLogService', 'Record every classification, human edit, notification and status transition.'),
        ],
        'admin_pages': [
            ('OpsDashboard', 'KPIs: missed calls captured, urgent jobs, recovered revenue, response time.'),
            ('CallQueue', 'Review all inbound call items with AI classification and confidence.'),
            ('CallDetail', 'Transcript, extracted fields, dispatch decision, edit history and notes.'),
            ('RoutingRules', 'Configure service areas, emergency categories and notification recipients.'),
            ('Analytics', 'Weekly recovery trends, lead source breakdown and missed opportunity value.'),
        ],
    },
    'property-maintenance-triage': {
        'name': 'Property Maintenance Triage',
        'domain': 'property managers / landlords',
        'frontend_pages': [
            ('Landing', 'Public page for reducing chaotic tenant maintenance messages.'),
            ('TenantRequestDemo', 'Show tenant issue submission and AI triage result.'),
            ('ROICalculator', 'Estimate manager time saved and emergency leakage reduction.'),
            ('PortfolioAuditForm', 'Collect unit count, channels used, issue volume and vendor process.'),
            ('PilotSignup', 'Book a workflow audit for a property manager.'),
        ],
        'backend_modules': [
            ('RequestIntakeService', 'Ingest tenant maintenance requests from form/email/manual entry.'),
            ('IssueClassifier', 'Classify plumbing/electrical/HVAC/appliance/general and emergency level.'),
            ('VendorRoutingEngine', 'Suggest vendor/category/routing path and next required info.'),
            ('TenantSummaryWriter', 'Produce manager/vendor-ready summaries without overpromising repair actions.'),
            ('SLAWatcher', 'Track status, response deadlines, escalations and unresolved items.'),
        ],
        'admin_pages': [
            ('PortfolioDashboard', 'Open issues, emergencies, aging tickets and vendor workload.'),
            ('RequestQueue', 'Triage queue with category, urgency and missing info.'),
            ('RequestDetail', 'Tenant message, extracted facts, suggested route and audit log.'),
            ('VendorSettings', 'Vendors by trade, coverage, availability and contact rules.'),
            ('SLAAnalytics', 'Resolution time, emergency rate and repeated-property issues.'),
        ],
    },
    'construction-bid-inbox': {
        'name': 'Construction Bid Inbox',
        'domain': 'small contractors / subcontractors',
        'frontend_pages': [
            ('Landing', 'Public page for turning chaotic bid requests into a clean bid pipeline.'),
            ('BidInboxDemo', 'Show an email/RFP transformed into structured scope and checklist.'),
            ('PipelineCalculator', 'Estimate admin hours saved and bid throughput increase.'),
            ('TradeFitForm', 'Collect trade, region, project size and current estimating workflow.'),
            ('PilotSignup', 'Invite contractors to a manual bid-inbox cleanup pilot.'),
        ],
        'backend_modules': [
            ('BidIntakeService', 'Ingest emails/manual bid requests and attachments metadata.'),
            ('ScopeExtractor', 'Extract trade, location, due date, scope, exclusions and missing files.'),
            ('BidFitScorer', 'Score fit based on geography, size, trade, deadline and risk.'),
            ('ChecklistGenerator', 'Generate estimator-ready missing-info/checklist notes.'),
            ('PipelineStatusService', 'Track new/reviewing/bid/no-bid/submitted/lost/won states.'),
        ],
        'admin_pages': [
            ('BidDashboard', 'Pipeline counts, due dates, potential value and bottlenecks.'),
            ('BidQueue', 'Prioritized bid inbox with fit score and deadline.'),
            ('BidDetail', 'Scope summary, missing docs, risks and estimator notes.'),
            ('NoBidRules', 'Configure bad-fit criteria and trade/geography limits.'),
            ('EstimatorAnalytics', 'Bid velocity, win/loss notes and opportunity value.'),
        ],
    },
    'dental-insurance-checklist': {
        'name': 'Dental Insurance Checklist',
        'domain': 'dental offices / insurance verification teams',
        'frontend_pages': [
            ('Landing', 'Public page around reducing insurance verification mistakes and rework.'),
            ('ChecklistDemo', 'Show a verification checklist generated from patient/procedure context.'),
            ('ReworkCalculator', 'Estimate admin time lost to missing insurance information.'),
            ('OfficeAuditForm', 'Collect office size, procedure mix and verification workflow.'),
            ('PilotSignup', 'Request a controlled checklist pilot.'),
        ],
        'backend_modules': [
            ('VerificationIntakeService', 'Capture patient/procedure/plan metadata without storing unnecessary PHI.'),
            ('ChecklistBuilder', 'Generate procedure-specific verification checklist and missing fields.'),
            ('PolicyLanguageSummarizer', 'Summarize plan notes into staff-readable reminders with source references.'),
            ('ComplianceGuard', 'Flag PHI/compliance-sensitive handling and avoid payment guarantees.'),
            ('VerificationAuditService', 'Track checklist completion, edits and verification status.'),
        ],
        'admin_pages': [
            ('VerificationDashboard', 'Pending verifications, completed checks and rework indicators.'),
            ('ChecklistQueue', 'Patients/procedures awaiting verification steps.'),
            ('ChecklistDetail', 'Checklist, source notes, completion state and staff comments.'),
            ('ProcedureTemplates', 'Configure checklist templates by procedure category.'),
            ('ComplianceLog', 'PHI access/change events and approval history.'),
        ],
    },
    'msp-security-reporting': {
        'name': 'MSP Security Reporting Copilot',
        'domain': 'managed service providers / vCISO services',
        'frontend_pages': [
            ('Landing', 'Public page for MSPs turning security work into client-ready reports.'),
            ('ReportBeforeAfter', 'Show raw security noise vs executive summary/report.'),
            ('ClientProofDemo', 'Demonstrate monthly client report generation and approval flow.'),
            ('StackAuditForm', 'Collect tools used, number of clients and reporting pain.'),
            ('PilotSignup', 'Invite MSPs to test on one anonymized client report.'),
        ],
        'backend_modules': [
            ('EvidenceImportService', 'Import CSV/manual evidence from security tools and ticket systems.'),
            ('SignalNormalizer', 'Normalize findings, alerts, tickets and remediation evidence.'),
            ('RiskNarrativeWriter', 'Draft executive-friendly summary with technical appendix.'),
            ('ClientReportGenerator', 'Assemble report sections, metrics, risks and next actions.'),
            ('ApprovalAuditService', 'Track edits, approvals, exports and client delivery status.'),
        ],
        'admin_pages': [
            ('ClientDashboard', 'Client accounts, report status, risk trends and pending approvals.'),
            ('EvidenceQueue', 'Imported findings needing mapping or review.'),
            ('ReportBuilder', 'Editable report sections with AI suggestions and source links.'),
            ('TemplateSettings', 'Configure report templates, tone and risk language.'),
            ('DeliveryAudit', 'Export/delivery history and approval trace.'),
        ],
    },
    'med-spa-lead-recovery': {
        'name': 'Med Spa Lead Recovery',
        'domain': 'med spa / aesthetics clinics',
        'frontend_pages': [
            ('Landing', 'Public page for missed med-spa leads and consult booking leakage.'),
            ('LeadLeakCalculator', 'Estimate lost consult value from slow replies and missed DMs/calls.'),
            ('InstagramDMFlow', 'Demo DM/form/call captured into a consult follow-up queue.'),
            ('FreeLeadAuditForm', 'Collect services offered, lead sources and booking process.'),
            ('PilotSignup', 'Convert interested clinics into a follow-up pilot.'),
        ],
        'backend_modules': [
            ('LeadIntakeService', 'Ingest web forms, missed calls, SMS and manual DM exports.'),
            ('TreatmentIntentClassifier', 'Classify treatment interest, budget/timing and consult readiness.'),
            ('FollowupDraftService', 'Draft compliant consult booking messages for human approval.'),
            ('ComplianceLanguageGuard', 'Flag medical claims, guarantees and risky before/after wording.'),
            ('ConsultRevenueTracker', 'Track booked consults, no-shows and estimated recovered revenue.'),
        ],
        'admin_pages': [
            ('LeadDashboard', 'New leads, hot consults, booked consults and recovered value.'),
            ('LeadQueue', 'Prioritized follow-up queue by source and intent.'),
            ('LeadDetail', 'Contact data, service interest, notes, drafts and history.'),
            ('TreatmentSettings', 'Services, disclaimers, approved templates and routing rules.'),
            ('RevenueAnalytics', 'Lead source performance, booking rate and lost/recovered value.'),
        ],
    },
    'law-firm-intake-triage': {
        'name': 'Law Firm Intake Triage',
        'domain': 'small law firms / legal intake',
        'frontend_pages': [
            ('Landing', 'Public page for attorney-ready intake summaries and after-hours capture.'),
            ('PracticeAreaDemo', 'Show inquiry categorized into practice area and intake checklist.'),
            ('IntakeQualityCalculator', 'Estimate staff/attorney time lost on low-quality intake.'),
            ('FirmAuditForm', 'Collect practice areas, inquiry volume and current intake flow.'),
            ('PilotSignup', 'Invite a firm to test on non-confidential/sample inquiries first.'),
        ],
        'backend_modules': [
            ('LegalInquiryIntakeService', 'Capture structured inquiry with disclaimers and consent.'),
            ('PracticeAreaClassifier', 'Categorize practice area, urgency and missing facts.'),
            ('AttorneySummaryWriter', 'Create factual attorney-ready summaries without legal advice.'),
            ('ConflictChecklistService', 'Flag conflict-check fields and jurisdiction questions.'),
            ('IntakeAuditService', 'Log access, edits, routing decisions and disclaimers accepted.'),
        ],
        'admin_pages': [
            ('IntakeDashboard', 'New inquiries, urgent matters, practice area mix and response times.'),
            ('InquiryQueue', 'Prioritized intake queue with fit/urgency indicators.'),
            ('InquiryDetail', 'Facts, summary, missing info, disclaimers and routing decision.'),
            ('PracticeRules', 'Practice areas, routing rules, rejected categories and disclaimers.'),
            ('ComplianceAudit', 'Access logs, summary edits and human review decisions.'),
        ],
    },
    'chiropractic-reactivation-engine': {
        'name': 'Chiropractic Patient Reactivation Engine',
        'domain': 'chiropractic clinics',
        'frontend_pages': [
            ('Landing', 'Public page for reactivating inactive patients without spam.'),
            ('RecoveryCalculator', 'Estimate recovered appointments from inactive patient list.'),
            ('CampaignPreview', 'Show patient segment and human-approved message flow.'),
            ('InactiveListAuditForm', 'Collect list size, visit recency and campaign history.'),
            ('PilotSignup', 'Request a limited reactivation pilot.'),
        ],
        'backend_modules': [
            ('PatientListImportService', 'Import sanitized inactive-patient CSV and validate fields.'),
            ('ReactivationSegmenter', 'Segment by recency, visit type, last status and consent/eligibility.'),
            ('MessageDraftService', 'Draft gentle rebooking/nurture messages for staff approval.'),
            ('OptOutSuppressionService', 'Track opt-outs and suppress future contact.'),
            ('RecoveredAppointmentTracker', 'Track replies, booked appointments and recovery metrics.'),
        ],
        'admin_pages': [
            ('ReactivationDashboard', 'Segments, scheduled messages, replies and recovered appointments.'),
            ('SegmentBuilder', 'Build and review inactive patient cohorts.'),
            ('CampaignApproval', 'Review/edit/approve message drafts before sending.'),
            ('ReplyInbox', 'Track patient replies, booked, no response, opt-out.'),
            ('ComplianceLog', 'Data import, consent, opt-out and approval audit events.'),
        ],
    },
    'restaurant-catering-followup': {
        'name': 'Restaurant Catering Follow-Up Copilot',
        'domain': 'restaurants / catering sales',
        'frontend_pages': [
            ('Landing', 'Public page for recovering catering inquiries before they go cold.'),
            ('EventInquiryDemo', 'Show an inquiry parsed into event requirements and follow-up tasks.'),
            ('CateringRevenueCalculator', 'Estimate lost booked catering from slow replies.'),
            ('InboxAuditForm', 'Collect inquiry channels, weekly volume, average event value.'),
            ('PilotSignup', 'Invite restaurants to a catering inbox cleanup pilot.'),
        ],
        'backend_modules': [
            ('CateringInquiryIntakeService', 'Capture catering inquiry from form/email/manual entry.'),
            ('EventDetailsExtractor', 'Extract date, guests, budget, location, menu needs and constraints.'),
            ('FollowupReminderEngine', 'Create follow-up tasks and reminders based on lead status.'),
            ('QuoteChecklistBuilder', 'Generate missing info checklist before quoting.'),
            ('BookedRevenueTracker', 'Track quoted/booked/lost catering revenue.'),
        ],
        'admin_pages': [
            ('CateringDashboard', 'New inquiries, quotes due, booked revenue and lost value.'),
            ('LeadBoard', 'Kanban by new/contacted/quoted/booked/lost.'),
            ('EventDetail', 'Event requirements, quote checklist, notes and follow-up history.'),
            ('MenuPackageSettings', 'Configure packages, menus, capacity and service areas.'),
            ('RevenueAnalytics', 'Inquiry source, booking rate, average event value.'),
        ],
    },
    'b2b-podcast-repurposing-system': {
        'name': 'B2B Podcast Repurposing System',
        'domain': 'B2B founders / content teams',
        'frontend_pages': [
            ('Landing', 'Public page for turning one B2B conversation into a week of content.'),
            ('BeforeAfterDemo', 'Show transcript fragment transformed into posts/thread/newsletter.'),
            ('TranscriptUploadDemo', 'Demo source upload/paste and output selection.'),
            ('ContentCalendarPreview', 'Show generated weekly publishing queue.'),
            ('EpisodeAuditForm', 'Collect audience, channel, tone and sample transcript.'),
        ],
        'backend_modules': [
            ('TranscriptIngestionService', 'Accept transcript text/notes and chunk into sections.'),
            ('InsightExtractor', 'Extract stories, claims, objections, frameworks and quotable moments.'),
            ('ChannelDraftGenerator', 'Generate LinkedIn, X, email and blog drafts by channel constraints.'),
            ('VoiceConsistencyScorer', 'Score drafts for founder voice, specificity and AI-generic language.'),
            ('PublishingQueueService', 'Create approval queue and calendar-ready content items.'),
        ],
        'admin_pages': [
            ('ContentDashboard', 'Sources, drafts, approvals and publishing queue.'),
            ('SourceLibrary', 'Transcripts/notes with extracted themes and status.'),
            ('DraftWorkspace', 'Edit drafts, regenerate sections and compare variants.'),
            ('VoiceSettings', 'Audience, tone, banned phrases, examples and CTA preferences.'),
            ('CalendarBoard', 'Scheduled/approved/published content by channel.'),
        ],
    },
}

component_template = """# {title}\n\n## Purpose\n\n{purpose}\n\n## Primary states\n\n- Empty\n- Loading\n- Ready\n- Needs review\n- Error\n\n## Data needed\n\n- tenant_id/account context\n- authenticated user role where private/admin\n- item/list/query params relevant to this view/module\n\n## UX / logic notes\n\n- Keep actions explicit and reversible in MVP.\n- Show confidence or status where AI is involved.\n- Never hide human-review requirements behind automation language.\n"""

backend_template = """# {title}\n\n## Responsibility\n\n{purpose}\n\n## Input\n\n- validated request/event payload\n- tenant/account context\n- authenticated actor where required\n\n## Output\n\n- structured domain object or status update\n- audit event\n- low-confidence/review flags when applicable\n\n## Security notes\n\n- validate all external input\n- do not trust LLM/user-provided text as instructions\n- avoid secrets in logs\n- write audit events for sensitive actions\n"""

admin_template = """# {title}\n\n## Purpose\n\n{purpose}\n\n## Operators\n\n- owner/admin\n- staff/reviewer\n- auditor/compliance role where relevant\n\n## Actions\n\n- view\n- filter\n- edit/review\n- approve/reject\n- export/report where safe\n\n## Guardrails\n\n- destructive actions require confirmation\n- AI suggestions are labeled as suggestions\n- all status/rule changes are audit logged\n"""

for slug, b in businesses.items():
    br = root / slug
    if not br.exists():
        continue
    # Shared implementation plan
    (br / 'IMPLEMENTATION_TRACK.md').write_text(dedent(f"""
    # Implementation Track — {b['name']}

    This file is the agent handoff for building this business one layer at a time.

    ## Build order

    1. Frontend public validation surfaces.
    2. Backend motor and API contracts.
    3. Admin/control panel.
    4. Internal AI orchestration with human review.
    5. Security hardening and audit logs.

    ## Current build mode

    Internal scaffold only inside `output/businesses/{slug}`. No deploy, no production secrets, no GitHub split yet.

    ## Domain

    {b['domain']}
    """).strip() + '\n')

    # Frontend files
    frontend_dir = br / 'frontend' / 'src' / 'views'
    frontend_dir.mkdir(parents=True, exist_ok=True)
    (br / 'frontend' / 'ROUTES.md').write_text('# Frontend Routes\n\n' + '\n'.join([f"- `/{slug}/{name.lower().replace(' ', '-')}` — {desc}" for name, desc in b['frontend_pages']]) + '\n')
    for name, desc in b['frontend_pages']:
        (frontend_dir / f'{name}.md').write_text(component_template.format(title=f'Frontend View — {name}', purpose=desc))

    # Backend files
    backend_dir = br / 'backend' / 'src' / 'modules'
    backend_dir.mkdir(parents=True, exist_ok=True)
    (br / 'backend' / 'SERVICES.md').write_text('# Backend Services\n\n' + '\n'.join([f"- `{name}` — {desc}" for name, desc in b['backend_modules']]) + '\n')
    for name, desc in b['backend_modules']:
        (backend_dir / f'{name}.md').write_text(backend_template.format(title=f'Backend Module — {name}', purpose=desc))

    # Admin files
    admin_dir = br / 'admin' / 'src' / 'views'
    admin_dir.mkdir(parents=True, exist_ok=True)
    (br / 'admin' / 'ROUTES.md').write_text('# Admin Routes\n\n' + '\n'.join([f"- `/admin/{slug}/{name.lower().replace(' ', '-')}` — {desc}" for name, desc in b['admin_pages']]) + '\n')
    for name, desc in b['admin_pages']:
        (admin_dir / f'{name}.md').write_text(admin_template.format(title=f'Admin View — {name}', purpose=desc))

    # Layer readme
    (br / 'LAYER_PROGRESS.md').write_text(dedent(f"""
    # Layer Progress — {b['name']}

    ## Frontend

    {chr(10).join('- ' + name + ': ' + desc for name, desc in b['frontend_pages'])}

    ## Backend motor

    {chr(10).join('- ' + name + ': ' + desc for name, desc in b['backend_modules'])}

    ## Admin panel

    {chr(10).join('- ' + name + ': ' + desc for name, desc in b['admin_pages'])}

    ## Next implementation step

    Convert these markdown scaffolds into real app files only after Andre selects this business for repo split/build.
    """).strip() + '\n')

# Progress index
lines = ['# One-by-One Build Progress', '', 'Each business now has explicit frontend routes/views, backend services/modules, and admin routes/views.', '']
for slug, b in businesses.items():
    br = root / slug
    if br.exists():
        fv = len(list((br/'frontend/src/views').glob('*.md')))
        bm = len(list((br/'backend/src/modules').glob('*.md')))
        av = len(list((br/'admin/src/views').glob('*.md')))
        lines.append(f'- `{slug}` — frontend views: {fv}, backend modules: {bm}, admin views: {av}')
(root / 'ONE_BY_ONE_PROGRESS.md').write_text('\n'.join(lines) + '\n')

print('deepened', len([slug for slug in businesses if (root/slug).exists()]), 'businesses')
