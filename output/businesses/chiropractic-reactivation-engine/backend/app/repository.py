"""Repository contracts for Chiropractic Reactivation Engine.

MongoDB is the intended database, but this file deliberately does not open a
Mongo connection yet. The in-memory repository lets the API run locally and
gives us a stable boundary to swap in Motor/PyMongo later.
"""
from app.schemas import AssessmentResult, IntakeRecord


class MongoCollections:
    intakes = "reactivation_candidate_intakes"
    assessments = "reactivation_candidate_assessments"
    audit_events = "audit_events"


class InMemoryRepository:
    def __init__(self) -> None:
        self.intakes: dict[str, IntakeRecord] = {}
        self.assessments: dict[str, AssessmentResult] = {}

    def create_intake(self, intake: IntakeRecord) -> IntakeRecord:
        self.intakes[intake.id] = intake
        return intake

    def get_intake(self, intake_id: str) -> IntakeRecord | None:
        return self.intakes.get(intake_id)

    def list_intakes(self) -> list[IntakeRecord]:
        return list(self.intakes.values())

    def save_assessment(self, assessment: AssessmentResult) -> AssessmentResult:
        self.assessments[assessment.id] = assessment
        return assessment


repository = InMemoryRepository()
