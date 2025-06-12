from fastapi import APIRouter
from app.schemas import ConversationCreate
from app.services import create_conversation

router = APIRouter()

@router.post("/")
def create_conversation_route(conv: ConversationCreate):
    conv_id = create_conversation(conv)
    return {"id": conv_id}