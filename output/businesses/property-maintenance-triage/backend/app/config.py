"""Runtime settings for Property Maintenance Triage."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="PROPERTY_MAINTENANCE_TRIAGE_", extra="ignore")

    app_name: str = "Property Maintenance Triage API"
    app_version: str = "0.1.0"
    business_slug: str = "property-maintenance-triage"
    description: str = "FastAPI backend scaffold for property managers and maintenance coordinators — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "property_maintenance_triage"
    mongo_collection_intakes: str = "triage_ticket_intakes"
    mongo_collection_assessments: str = "triage_ticket_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
