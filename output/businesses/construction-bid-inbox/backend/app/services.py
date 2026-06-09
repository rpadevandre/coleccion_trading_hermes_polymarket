"""Business services for Construction Bid Inbox."""
from app.repository import repository
from app.schemas import AssessmentRequest, AssessmentResult, IntakeCreate, IntakeRecord, Priority, QueueItem

AI_MODULES = ['BidIntakeService', 'ScopeExtractor', 'BidFitScorer', 'ChecklistGenerator', 'PipelineStatusService']
EXPECTED_SIGNALS = ['trade', 'deadline', 'project_location', 'scope_text', 'estimated_value']


def create_intake(payload: IntakeCreate) -> IntakeRecord:
    return repository.create_intake(IntakeRecord(**payload.model_dump()))


def get_intake(intake_id: str) -> IntakeRecord | None:
    return repository.get_intake(intake_id)


def list_intakes() -> list[IntakeRecord]:
    return repository.list_intakes()


def assess(payload: AssessmentRequest) -> AssessmentResult:
    text = f"{payload.message} {payload.human_context or ''}".lower()
    missing = [field for field in EXPECTED_SIGNALS if field not in payload.signals]
    risk_flags: list[str] = []
    score = 45

    urgent_terms = ["urgent", "emergency", "deadline", "today", "asap", "lost", "risk", "high value"]
    if any(term in text for term in urgent_terms):
        score += 25
        priority = Priority.high
    else:
        priority = Priority.medium

    if payload.signals:
        score += min(20, len(payload.signals) * 4)
    if len(missing) <= max(1, len(EXPECTED_SIGNALS) // 2):
        score += 10
    if "unsubscribe" in text or "do not contact" in text:
        risk_flags.append("possible_opt_out_or_suppression_required")
        score = min(score, 40)
        priority = Priority.low

    score = max(0, min(100, score))
    if score >= 80:
        next_action = "route_to_human_operator_for_same_day_followup"
    elif score >= 60:
        next_action = "collect_missing_information_then_prepare_followup"
    else:
        next_action = "hold_for_manual_review_or_low_priority_batch"

    result = AssessmentResult(
        intake_id=payload.intake_id,
        score=score,
        priority=priority,
        summary="Construction Bid Inbox assessment for bid invitations scattered across emails/portals with unclear trade fit and deadlines.",
        recommended_next_action=next_action,
        risk_flags=risk_flags,
        missing_information=missing,
        ai_modules_to_run=AI_MODULES,
    )
    return repository.save_assessment(result)


def admin_queue() -> list[QueueItem]:
    items: list[QueueItem] = []
    for intake in repository.list_intakes():
        items.append(
            QueueItem(
                id=intake.id,
                priority=intake.priority,
                status=intake.status,
                contact_name=intake.contact_name,
                company_or_location=intake.company_or_location,
                message_preview=intake.message[:140],
                next_action="run_assessment_then_route_to_bid_review_queue",
            )
        )
    return items
