from fastapi import APIRouter, HTTPException
from app.schemas import MessageCreate, Message
from app.services import message_service

message_routes = APIRouter()

@message_routes.post("/messages")
def create_message(message: MessageCreate):
    return message_service.create_message(message)