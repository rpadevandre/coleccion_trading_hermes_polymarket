"""Runtime settings for Construction Bid Inbox."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CONSTRUCTION_BID_INBOX_", extra="ignore")

    app_name: str = "Construction Bid Inbox API"
    app_version: str = "0.1.0"
    business_slug: str = "construction-bid-inbox"
    description: str = "FastAPI backend scaffold for contractors and subcontractor estimating teams — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "construction_bid_inbox"
    mongo_collection_intakes: str = "bid_opportunity_intakes"
    mongo_collection_assessments: str = "bid_opportunity_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
