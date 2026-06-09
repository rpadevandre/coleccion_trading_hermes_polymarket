"""Runtime settings for Restaurant Catering Followup."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="RESTAURANT_CATERING_FOLLOWUP_", extra="ignore")

    app_name: str = "Restaurant Catering Followup API"
    app_version: str = "0.1.0"
    business_slug: str = "restaurant-catering-followup"
    description: str = "FastAPI backend scaffold for restaurants with catering/event programs — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "restaurant_catering_followup"
    mongo_collection_intakes: str = "catering_opportunity_intakes"
    mongo_collection_assessments: str = "catering_opportunity_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
