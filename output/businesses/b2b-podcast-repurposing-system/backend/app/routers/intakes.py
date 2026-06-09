from fastapi import APIRouter, HTTPException

from app.schemas import IntakeCreate, IntakeRecord
from app.services import create_intake, get_intake, list_intakes

router = APIRouter()


@router.post("", response_model=IntakeRecord, status_code=201)
def create(payload: IntakeCreate) -> IntakeRecord:
    return create_intake(payload)


@router.get("", response_model=list[IntakeRecord])
def list_all() -> list[IntakeRecord]:
    return list_intakes()


@router.get("/{intake_id}", response_model=IntakeRecord)
def retrieve(intake_id: str) -> IntakeRecord:
    intake = get_intake(intake_id)
    if intake is None:
        raise HTTPException(status_code=404, detail="intake_not_found")
    return intake
