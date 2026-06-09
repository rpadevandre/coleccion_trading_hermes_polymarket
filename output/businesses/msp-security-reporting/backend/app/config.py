"""Runtime settings for MSP Security Reporting."""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="MSP_SECURITY_REPORTING_", extra="ignore")

    app_name: str = "MSP Security Reporting API"
    app_version: str = "0.1.0"
    business_slug: str = "msp-security-reporting"
    description: str = "FastAPI backend scaffold for MSPs, vCISO providers, and IT consultants — no database connection enabled yet."
    environment: str = "local"
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173", "http://localhost:3000"])

    # Mongo-ready placeholders. Do not set real credentials in git.
    mongo_uri: str | None = None
    mongo_database: str = "msp_security_reporting"
    mongo_collection_intakes: str = "client_report_case_intakes"
    mongo_collection_assessments: str = "client_report_case_assessments"
    mongo_collection_audit_events: str = "audit_events"
    enable_mongo: bool = False


settings = Settings()
