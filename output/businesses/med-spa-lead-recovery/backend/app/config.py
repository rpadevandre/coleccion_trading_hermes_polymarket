"""Runtime settings for Med Spa Lead Recovery."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="MED_SPA_LEAD_RECOVERY_", extra="ignore")

    app_name: str = "Med Spa Lead Recovery API"
    app_version: str = "0.1.0"
    business_slug: str = "med-spa-lead-recovery"
    description: str = "FastAPI backend scaffold for med spas and aesthetic clinics — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "med_spa_lead_recovery"
    mongo_collection_intakes: str = "recovery_opportunity_intakes"
    mongo_collection_assessments: str = "recovery_opportunity_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
