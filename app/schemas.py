from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class ConversationCreate(BaseModel):
    user1_id: int
    user2_id: int

class MessageCreate(BaseModel):
    sender_id: int
    receiver_id: int
    content: str