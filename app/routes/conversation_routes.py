from fastapi import APIRouter

conversation_routes = APIRouter()

@conversation_routes.get("/")
async def read_conversations():
    return {"message": "Conversation route operational"}