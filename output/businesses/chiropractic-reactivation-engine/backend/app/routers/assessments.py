from fastapi import APIRouter

from app.schemas import AssessmentRequest, AssessmentResult
from app.services import assess

router = APIRouter()


@router.post("/score", response_model=AssessmentResult)
def score(payload: AssessmentRequest) -> AssessmentResult:
    return assess(payload)
