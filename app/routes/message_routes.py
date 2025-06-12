from fastapi import APIRouter

message_routes = APIRouter()

@message_routes.get("/messages")
def get_messages():
    return {"message": "Message list"}