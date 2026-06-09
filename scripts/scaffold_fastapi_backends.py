#!/usr/bin/env python3
"""Generate FastAPI backend scaffolds for each incubated business.

No database connections are opened here. Each backend is Mongo-ready by contract:
settings expose a MONGO_URI placeholder, repository classes document collection names,
and all runtime storage uses an in-memory repository until Andre approves real MongoDB.
"""
from __future__ import annotations

from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parents[1] / "output" / "businesses"

BUSINESSES = {
    "hvac-missed-call-recovery": {
        "title": "HVAC Missed-Call Recovery",
        "domain": "HVAC service companies",
        "primary_intake": "missed_call",
        "entity": "recovery_lead",
        "pain": "missed calls, after-hours requests, and unprioritized emergency leads",
        "modules": ["CallIntakeService", "UrgencyClassifier", "RevenueEstimator", "DispatchRouter", "AuditLogService"],
        "signals": ["call_time", "service_type", "after_hours", "zip_code", "customer_message"],
        "queue": "dispatch_recovery_queue",
    },
    "property-maintenance-triage": {
        "title": "Property Maintenance Triage",
        "domain": "property managers and maintenance coordinators",
        "primary_intake": "maintenance_request",
        "entity": "triage_ticket",
        "pain": "vague tenant repair requests, urgency confusion, and vendor routing overhead",
        "modules": ["RequestIntakeService", "IssueClassifier", "VendorRoutingEngine", "TenantSummaryWriter", "SLAWatcher"],
        "signals": ["unit_id", "issue_category", "photos_available", "after_hours", "tenant_message"],
        "queue": "maintenance_triage_queue",
    },
    "construction-bid-inbox": {
        "title": "Construction Bid Inbox",
        "domain": "contractors and subcontractor estimating teams",
        "primary_intake": "bid_invitation",
        "entity": "bid_opportunity",
        "pain": "bid invitations scattered across emails/portals with unclear trade fit and deadlines",
        "modules": ["BidIntakeService", "ScopeExtractor", "BidFitScorer", "ChecklistGenerator", "PipelineStatusService"],
        "signals": ["trade", "deadline", "project_location", "scope_text", "estimated_value"],
        "queue": "bid_review_queue",
    },
    "dental-insurance-checklist": {
        "title": "Dental Insurance Checklist",
        "domain": "dental offices and treatment coordinators",
        "primary_intake": "insurance_verification",
        "entity": "verification_case",
        "pain": "insurance verification mistakes that delay care, claims, and revenue collection",
        "modules": ["VerificationIntakeService", "ChecklistBuilder", "PolicyLanguageSummarizer", "ComplianceGuard", "VerificationAuditService"],
        "signals": ["payer", "procedure_type", "appointment_date", "missing_fields", "verification_notes"],
        "queue": "verification_review_queue",
    },
    "msp-security-reporting": {
        "title": "MSP Security Reporting",
        "domain": "MSPs, vCISO providers, and IT consultants",
        "primary_intake": "security_evidence",
        "entity": "client_report_case",
        "pain": "technical security evidence that is hard to convert into client-friendly reporting",
        "modules": ["EvidenceImportService", "SignalNormalizer", "RiskNarrativeWriter", "ClientReportGenerator", "ApprovalAuditService"],
        "signals": ["client_name", "finding_type", "severity", "evidence_summary", "recommended_action"],
        "queue": "reporting_review_queue",
    },
    "med-spa-lead-recovery": {
        "title": "Med Spa Lead Recovery",
        "domain": "med spas and aesthetic clinics",
        "primary_intake": "consult_lead",
        "entity": "recovery_opportunity",
        "pain": "consult requests across calls, forms, DMs, and SMS that never become bookings",
        "modules": ["LeadIntakeService", "TreatmentIntentClassifier", "FollowupDraftService", "ComplianceLanguageGuard", "ConsultRevenueTracker"],
        "signals": ["lead_source", "treatment_interest", "message", "last_contacted_at", "booking_status"],
        "queue": "consult_recovery_queue",
    },
    "law-firm-intake-triage": {
        "title": "Law Firm Intake Triage",
        "domain": "small law firms and intake teams",
        "primary_intake": "legal_inquiry",
        "entity": "intake_case",
        "pain": "poor-fit inquiries and urgent potential cases mixed together in intake channels",
        "modules": ["LegalInquiryIntakeService", "PracticeAreaClassifier", "ConflictChecklistService", "AttorneySummaryWriter", "IntakeAuditService"],
        "signals": ["practice_area", "deadline", "jurisdiction", "opposing_party", "inquiry_summary"],
        "queue": "attorney_review_queue",
    },
    "chiropractic-reactivation-engine": {
        "title": "Chiropractic Reactivation Engine",
        "domain": "chiropractic clinics",
        "primary_intake": "inactive_patient_segment",
        "entity": "reactivation_candidate",
        "pain": "inactive patients who could return but are not followed up systematically",
        "modules": ["PatientListImportService", "ReactivationSegmenter", "MessageDraftService", "OptOutSuppressionService", "RecoveredAppointmentTracker"],
        "signals": ["last_visit_date", "patient_status", "preferred_channel", "care_plan_stage", "opt_out_status"],
        "queue": "reactivation_review_queue",
    },
    "restaurant-catering-followup": {
        "title": "Restaurant Catering Followup",
        "domain": "restaurants with catering/event programs",
        "primary_intake": "catering_inquiry",
        "entity": "catering_opportunity",
        "pain": "catering/event inquiries that are not qualified or followed up quickly enough",
        "modules": ["CateringInquiryIntakeService", "EventDetailsExtractor", "QuoteChecklistBuilder", "FollowupReminderEngine", "BookedRevenueTracker"],
        "signals": ["event_date", "guest_count", "budget", "event_type", "contact_message"],
        "queue": "catering_followup_queue",
    },
    "b2b-podcast-repurposing-system": {
        "title": "B2B Podcast Repurposing System",
        "domain": "B2B founders, consultants, and content teams",
        "primary_intake": "content_episode",
        "entity": "repurposing_job",
        "pain": "valuable podcast/call transcripts that do not become reusable sales/content assets",
        "modules": ["TranscriptIngestionService", "InsightExtractor", "ChannelDraftGenerator", "VoiceConsistencyScorer", "PublishingQueueService"],
        "signals": ["episode_title", "transcript_summary", "target_channel", "buyer_persona", "campaign_goal"],
        "queue": "content_asset_queue",
    },
}


def py_list(values: list[str]) -> str:
    return "[" + ", ".join(repr(v) for v in values) + "]"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def main_py(slug: str, cfg: dict) -> str:
    return f'''
    """FastAPI entrypoint for {cfg["title"]}.

    Database status: Mongo-ready contract only. This app intentionally uses an
    in-memory repository until MongoDB credentials, collections, indexes, and
    retention rules are approved.
    """
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware

    from app.config import settings
    from app.routers import admin, assessments, health, intakes


    def create_app() -> FastAPI:
        app = FastAPI(
            title=settings.app_name,
            version=settings.app_version,
            description=settings.description,
            docs_url="/docs",
            redoc_url="/redoc",
        )
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        app.include_router(health.router)
        app.include_router(intakes.router, prefix="/intakes", tags=["intakes"])
        app.include_router(assessments.router, prefix="/assessments", tags=["assessments"])
        app.include_router(admin.router, prefix="/admin", tags=["admin"])
        return app


    app = create_app()
    '''


def config_py(slug: str, cfg: dict) -> str:
    return f'''
    """Runtime settings for {cfg["title"]}."""
    from pydantic import Field
    from pydantic_settings import BaseSettings, SettingsConfigDict


    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file=".env", env_prefix="{slug.replace('-', '_').upper()}_", extra="ignore")

        app_name: str = "{cfg['title']} API"
        app_version: str = "0.1.0"
        business_slug: str = "{slug}"
        description: str = "FastAPI backend scaffold for {cfg['domain']} — no database connection enabled yet."
        environment: str = "local"
        allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

        # Mongo-ready placeholders. Do not set real credentials in git.
        mongo_uri: str | None = None
        mongo_database: str = "{slug.replace('-', '_')}"
        mongo_collection_intakes: str = "{cfg['entity']}_intakes"
        mongo_collection_assessments: str = "{cfg['entity']}_assessments"
        mongo_collection_audit_events: str = "audit_events"
        enable_mongo: bool = False


    settings = Settings()
    '''


def schemas_py(cfg: dict) -> str:
    return f'''
    """Pydantic API contracts for {cfg["title"]}."""
    from datetime import datetime, timezone
    from enum import Enum
    from typing import Any
    from uuid import uuid4

    from pydantic import BaseModel, Field


    class Priority(str, Enum):
        low = "low"
        medium = "medium"
        high = "high"
        urgent = "urgent"


    class IntakeStatus(str, Enum):
        new = "new"
        triaged = "triaged"
        needs_human_review = "needs_human_review"
        ready_for_followup = "ready_for_followup"
        closed = "closed"


    class IntakeCreate(BaseModel):
        source: str = Field(..., examples=["website_form", "phone", "email", "manual_upload"])
        contact_name: str | None = None
        contact_email: str | None = None
        contact_phone: str | None = None
        company_or_location: str | None = None
        message: str = Field(..., min_length=3)
        signals: dict[str, Any] = Field(default_factory=dict, description="Business-specific extracted fields: {', '.join(cfg['signals'])}.")
        consent_for_followup: bool = False


    class IntakeRecord(IntakeCreate):
        id: str = Field(default_factory=lambda: str(uuid4()))
        business_entity: str = "{cfg['entity']}"
        status: IntakeStatus = IntakeStatus.new
        priority: Priority = Priority.medium
        created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
        updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


    class AssessmentRequest(BaseModel):
        intake_id: str | None = None
        message: str
        signals: dict[str, Any] = Field(default_factory=dict)
        human_context: str | None = None


    class AssessmentResult(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid4()))
        intake_id: str | None = None
        score: int = Field(..., ge=0, le=100)
        priority: Priority
        summary: str
        recommended_next_action: str
        risk_flags: list[str] = Field(default_factory=list)
        missing_information: list[str] = Field(default_factory=list)
        ai_modules_to_run: list[str] = Field(default_factory=list)
        created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


    class QueueItem(BaseModel):
        id: str
        priority: Priority
        status: IntakeStatus
        contact_name: str | None
        company_or_location: str | None
        message_preview: str
        next_action: str
    '''


def repository_py(cfg: dict) -> str:
    return f'''
    """Repository contracts for {cfg["title"]}.

    MongoDB is the intended database, but this file deliberately does not open a
    Mongo connection yet. The in-memory repository lets the API run locally and
    gives us a stable boundary to swap in Motor/PyMongo later.
    """
    from app.schemas import AssessmentResult, IntakeRecord


    class MongoCollections:
        intakes = "{cfg['entity']}_intakes"
        assessments = "{cfg['entity']}_assessments"
        audit_events = "audit_events"


    class InMemoryRepository:
        def __init__(self) -> None:
            self.intakes: dict[str, IntakeRecord] = {{}}
            self.assessments: dict[str, AssessmentResult] = {{}}

        def create_intake(self, intake: IntakeRecord) -> IntakeRecord:
            self.intakes[intake.id] = intake
            return intake

        def get_intake(self, intake_id: str) -> IntakeRecord | None:
            return self.intakes.get(intake_id)

        def list_intakes(self) -> list[IntakeRecord]:
            return list(self.intakes.values())

        def save_assessment(self, assessment: AssessmentResult) -> AssessmentResult:
            self.assessments[assessment.id] = assessment
            return assessment


    repository = InMemoryRepository()
    '''


def services_py(cfg: dict) -> str:
    modules = py_list(cfg["modules"])
    signals = py_list(cfg["signals"])
    return f'''
    """Business services for {cfg["title"]}."""
    from app.repository import repository
    from app.schemas import AssessmentRequest, AssessmentResult, IntakeCreate, IntakeRecord, Priority, QueueItem

    AI_MODULES = {modules}
    EXPECTED_SIGNALS = {signals}


    def create_intake(payload: IntakeCreate) -> IntakeRecord:
        return repository.create_intake(IntakeRecord(**payload.model_dump()))


    def get_intake(intake_id: str) -> IntakeRecord | None:
        return repository.get_intake(intake_id)


    def list_intakes() -> list[IntakeRecord]:
        return repository.list_intakes()


    def assess(payload: AssessmentRequest) -> AssessmentResult:
        text = f"{{payload.message}} {{payload.human_context or ''}}".lower()
        missing = [field for field in EXPECTED_SIGNALS if field not in payload.signals]
        risk_flags: list[str] = []
        score = 45

        urgent_terms = ["urgent", "emergency", "deadline", "today", "asap", "lost", "risk", "high value"]
        if any(term in text for term in urgent_terms):
            score += 25
            priority = Priority.high
        else:
            priority = Priority.medium

        if payload.signals:
            score += min(20, len(payload.signals) * 4)
        if len(missing) <= max(1, len(EXPECTED_SIGNALS) // 2):
            score += 10
        if "unsubscribe" in text or "do not contact" in text:
            risk_flags.append("possible_opt_out_or_suppression_required")
            score = min(score, 40)
            priority = Priority.low

        score = max(0, min(100, score))
        if score >= 80:
            next_action = "route_to_human_operator_for_same_day_followup"
        elif score >= 60:
            next_action = "collect_missing_information_then_prepare_followup"
        else:
            next_action = "hold_for_manual_review_or_low_priority_batch"

        result = AssessmentResult(
            intake_id=payload.intake_id,
            score=score,
            priority=priority,
            summary="{cfg['title']} assessment for {cfg['pain']}.",
            recommended_next_action=next_action,
            risk_flags=risk_flags,
            missing_information=missing,
            ai_modules_to_run=AI_MODULES,
        )
        return repository.save_assessment(result)


    def admin_queue() -> list[QueueItem]:
        items: list[QueueItem] = []
        for intake in repository.list_intakes():
            items.append(
                QueueItem(
                    id=intake.id,
                    priority=intake.priority,
                    status=intake.status,
                    contact_name=intake.contact_name,
                    company_or_location=intake.company_or_location,
                    message_preview=intake.message[:140],
                    next_action="run_assessment_then_route_to_{cfg['queue']}",
                )
            )
        return items
    '''


def router_health(slug: str, cfg: dict) -> str:
    return f'''
    from fastapi import APIRouter

    from app.config import settings
    from app.services import AI_MODULES, EXPECTED_SIGNALS

    router = APIRouter(tags=["health"])


    @router.get("/health")
    def health() -> dict[str, object]:
        return {{
            "status": "ok",
            "business_slug": settings.business_slug,
            "mongo_enabled": settings.enable_mongo,
            "database_mode": "in_memory_until_mongo_is_approved",
        }}


    @router.get("/meta")
    def meta() -> dict[str, object]:
        return {{
            "title": settings.app_name,
            "domain": "{cfg['domain']}",
            "primary_intake": "{cfg['primary_intake']}",
            "business_entity": "{cfg['entity']}",
            "expected_signals": EXPECTED_SIGNALS,
            "ai_modules": AI_MODULES,
            "mongo_collections": {{
                "intakes": settings.mongo_collection_intakes,
                "assessments": settings.mongo_collection_assessments,
                "audit_events": settings.mongo_collection_audit_events,
            }},
        }}
    '''


def router_intakes() -> str:
    return '''
    from fastapi import APIRouter, HTTPException

    from app.schemas import IntakeCreate, IntakeRecord
    from app.services import create_intake, get_intake, list_intakes

    router = APIRouter()


    @router.post("", response_model=IntakeRecord, status_code=201)
    def create(payload: IntakeCreate) -> IntakeRecord:
        return create_intake(payload)


    @router.get("", response_model=list[IntakeRecord])
    def list_all() -> list[IntakeRecord]:
        return list_intakes()


    @router.get("/{intake_id}", response_model=IntakeRecord)
    def retrieve(intake_id: str) -> IntakeRecord:
        intake = get_intake(intake_id)
        if intake is None:
            raise HTTPException(status_code=404, detail="intake_not_found")
        return intake
    '''


def router_assessments() -> str:
    return '''
    from fastapi import APIRouter

    from app.schemas import AssessmentRequest, AssessmentResult
    from app.services import assess

    router = APIRouter()


    @router.post("/score", response_model=AssessmentResult)
    def score(payload: AssessmentRequest) -> AssessmentResult:
        return assess(payload)
    '''


def router_admin() -> str:
    return '''
    from fastapi import APIRouter

    from app.schemas import QueueItem
    from app.services import admin_queue

    router = APIRouter()


    @router.get("/queue", response_model=list[QueueItem])
    def queue() -> list[QueueItem]:
        return admin_queue()
    '''


def readme(slug: str, cfg: dict) -> str:
    return f'''
    # {cfg['title']} — FastAPI Backend

    This is the first executable backend scaffold for **{cfg['title']}**.

    ## Current status

    - Framework: Python + FastAPI.
    - Database: MongoDB planned, **not connected yet**.
    - Current persistence: in-memory repository for local prototype validation.
    - Public API docs: `/docs` when running locally.

    ## Why no database connection yet

    Andre specified that each business will use MongoDB later, but the current
    step should advance backend structure without connecting databases. This
    keeps secrets, schemas, indexes, and retention policies out of the repo until
    the product direction is confirmed.

    ## Run locally

    ```bash
    cd output/businesses/{slug}/backend
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload --port 8000
    ```

    Open:

    ```text
    http://localhost:8000/docs
    http://localhost:8000/health
    http://localhost:8000/meta
    ```

    ## Core endpoints

    ```text
    GET  /health
    GET  /meta
    POST /intakes
    GET  /intakes
    GET  /intakes/{{intake_id}}
    POST /assessments/score
    GET  /admin/queue
    ```

    ## Planned Mongo collections

    ```text
    database: {slug.replace('-', '_')}
    intakes: {cfg['entity']}_intakes
    assessments: {cfg['entity']}_assessments
    audit_events: audit_events
    ```

    ## Business modules represented

    {chr(10).join(f'- `{m}`' for m in cfg['modules'])}

    ## Next backend step

    1. Add real unit tests with `pytest` + FastAPI `TestClient`.
    2. Add Mongo repository behind the current repository interface using Motor.
    3. Define Mongo indexes and retention rules.
    4. Add auth/tenant boundaries before any real customer data.
    '''


def env_example(slug: str, cfg: dict) -> str:
    prefix = slug.replace('-', '_').upper()
    return f'''
    # Local only. Do not commit real credentials.
    {prefix}_ENVIRONMENT=local
    {prefix}_ENABLE_MONGO=false
    {prefix}_MONGO_URI=
    {prefix}_MONGO_DATABASE={slug.replace('-', '_')}
    '''


def test_contract(slug: str, cfg: dict) -> str:
    return f'''
    """Static contract tests for {cfg["title"]} backend scaffold.

    These tests avoid importing FastAPI so they can run before dependencies are
    installed. Runtime API tests should be added once the backend is promoted
    from scaffold to active MVP.
    """
    from pathlib import Path


    ROOT = Path(__file__).resolve().parents[1]


    def test_required_files_exist() -> None:
        for relative in [
            "app/main.py",
            "app/config.py",
            "app/schemas.py",
            "app/services.py",
            "app/repository.py",
            "app/routers/health.py",
            "app/routers/intakes.py",
            "app/routers/assessments.py",
            "app/routers/admin.py",
            "requirements.txt",
            ".env.example",
        ]:
            assert (ROOT / relative).exists(), relative


    def test_mongo_is_documented_but_not_connected() -> None:
        config = (ROOT / "app/config.py").read_text(encoding="utf-8")
        repo = (ROOT / "app/repository.py").read_text(encoding="utf-8")
        assert "enable_mongo: bool = False" in config
        assert "mongo_uri" in config
        assert "InMemoryRepository" in repo
        assert "does not open a" in repo


    def test_business_specific_contract() -> None:
        meta = (ROOT / "app/routers/health.py").read_text(encoding="utf-8")
        assert "{cfg['primary_intake']}" in meta
        assert "{cfg['entity']}" in meta
    '''


def generate_backend(slug: str, cfg: dict) -> None:
    backend = BASE / slug / "backend"
    write(backend / "requirements.txt", """
    fastapi==0.115.6
    uvicorn[standard]==0.34.0
    pydantic==2.10.4
    pydantic-settings==2.7.1
    python-multipart==0.0.20
    """)
    write(backend / ".env.example", env_example(slug, cfg))
    write(backend / "README.md", readme(slug, cfg))
    write(backend / "app" / "__init__.py", f'"""{cfg["title"]} backend package."""\n')
    write(backend / "app" / "main.py", main_py(slug, cfg))
    write(backend / "app" / "config.py", config_py(slug, cfg))
    write(backend / "app" / "schemas.py", schemas_py(cfg))
    write(backend / "app" / "repository.py", repository_py(cfg))
    write(backend / "app" / "services.py", services_py(cfg))
    write(backend / "app" / "routers" / "__init__.py", '\"\"\"API routers.\"\"\"\n')
    write(backend / "app" / "routers" / "health.py", router_health(slug, cfg))
    write(backend / "app" / "routers" / "intakes.py", router_intakes())
    write(backend / "app" / "routers" / "assessments.py", router_assessments())
    write(backend / "app" / "routers" / "admin.py", router_admin())
    legacy_test = backend / "tests" / "test_contract.py"
    if legacy_test.exists():
        legacy_test.unlink()
    test_name = f"test_contract_{slug.replace('-', '_')}.py"
    write(backend / "tests" / test_name, test_contract(slug, cfg))


def main() -> None:
    for slug, cfg in BUSINESSES.items():
        generate_backend(slug, cfg)
    print(f"Generated FastAPI backend scaffolds for {len(BUSINESSES)} businesses.")


if __name__ == "__main__":
    main()
