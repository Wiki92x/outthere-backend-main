from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str

class User(UserCreate):
    id: int

class ConversationCreate(BaseModel):
    user1_id: int
    user2_id: int

class Conversation(ConversationCreate):
    id: int

class MessageCreate(BaseModel):
    conversation_id: int
    sender_id: int
    receiver_id: int
    content: str

class Message(MessageCreate):
    id: int