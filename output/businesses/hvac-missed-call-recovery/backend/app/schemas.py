"""Pydantic API contracts for HVAC Missed-Call Recovery."""
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
    signals: dict[str, Any] = Field(default_factory=dict, description="Business-specific extracted fields: call_time, service_type, after_hours, zip_code, customer_message.")
    consent_for_followup: bool = False


class IntakeRecord(IntakeCreate):
    id: str = Field(default_factory=lambda: str(uuid4()))
    business_entity: str = "recovery_lead"
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
