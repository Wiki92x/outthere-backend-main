from fastapi import APIRouter

conversation_routes = APIRouter()

@conversation_routes.get("/conversations")
def get_conversations():
    return {"message": "Conversation list"}