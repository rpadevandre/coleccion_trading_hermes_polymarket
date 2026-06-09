from fastapi import APIRouter

from app.schemas import QueueItem
from app.services import admin_queue

router = APIRouter()


@router.get("/queue", response_model=list[QueueItem])
def queue() -> list[QueueItem]:
    return admin_queue()
