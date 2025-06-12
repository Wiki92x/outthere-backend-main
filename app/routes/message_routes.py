from fastapi import APIRouter

message_routes = APIRouter()

@message_routes.get("/")
async def read_messages():
    return {"message": "Message route operational"}