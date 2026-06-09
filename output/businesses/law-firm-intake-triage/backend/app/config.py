"""Runtime settings for Law Firm Intake Triage."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="LAW_FIRM_INTAKE_TRIAGE_", extra="ignore")

    app_name: str = "Law Firm Intake Triage API"
    app_version: str = "0.1.0"
    business_slug: str = "law-firm-intake-triage"
    description: str = "FastAPI backend scaffold for small law firms and intake teams — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "law_firm_intake_triage"
    mongo_collection_intakes: str = "intake_case_intakes"
    mongo_collection_assessments: str = "intake_case_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
