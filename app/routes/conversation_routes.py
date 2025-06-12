from fastapi import APIRouter, HTTPException
from app.schemas import ConversationCreate, Conversation
from app.services import conversation_service

conversation_routes = APIRouter()

@conversation_routes.post("/conversations")
def create_conversation(conversation: ConversationCreate):
    return conversation_service.create_conversation(conversation)