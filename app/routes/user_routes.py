from fastapi import APIRouter

user_routes = APIRouter()

@user_routes.get("/")
async def read_users():
    return {"message": "User route operational"}