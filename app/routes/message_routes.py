from fastapi import APIRouter
from app.schemas import MessageCreate
from app.services import create_message

router = APIRouter()

@router.post("/")
def create_message_route(msg: MessageCreate):
    msg_id = create_message(msg)
    return {"id": msg_id}