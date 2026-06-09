"""Runtime settings for Dental Insurance Checklist."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="DENTAL_INSURANCE_CHECKLIST_", extra="ignore")

    app_name: str = "Dental Insurance Checklist API"
    app_version: str = "0.1.0"
    business_slug: str = "dental-insurance-checklist"
    description: str = "FastAPI backend scaffold for dental offices and treatment coordinators — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "dental_insurance_checklist"
    mongo_collection_intakes: str = "verification_case_intakes"
    mongo_collection_assessments: str = "verification_case_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
