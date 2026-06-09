from fastapi import APIRouter

from app.config import settings
from app.services import AI_MODULES, EXPECTED_SIGNALS

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "business_slug": settings.business_slug,
        "mongo_enabled": settings.enable_mongo,
        "database_mode": "in_memory_until_mongo_is_approved",
    }


@router.get("/meta")
def meta() -> dict[str, object]:
    return {
        "title": settings.app_name,
        "domain": "MSPs, vCISO providers, and IT consultants",
        "primary_intake": "security_evidence",
        "business_entity": "client_report_case",
        "expected_signals": EXPECTED_SIGNALS,
        "ai_modules": AI_MODULES,
        "mongo_collections": {
            "intakes": settings.mongo_collection_intakes,
            "assessments": settings.mongo_collection_assessments,
            "audit_events": settings.mongo_collection_audit_events,
        },
    }
