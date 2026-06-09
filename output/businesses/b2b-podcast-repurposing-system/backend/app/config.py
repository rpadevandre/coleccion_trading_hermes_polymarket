"""Runtime settings for B2B Podcast Repurposing System."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="B2B_PODCAST_REPURPOSING_SYSTEM_", extra="ignore")

    app_name: str = "B2B Podcast Repurposing System API"
    app_version: str = "0.1.0"
    business_slug: str = "b2b-podcast-repurposing-system"
    description: str = "FastAPI backend scaffold for B2B founders, consultants, and content teams — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "b2b_podcast_repurposing_system"
    mongo_collection_intakes: str = "repurposing_job_intakes"
    mongo_collection_assessments: str = "repurposing_job_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
