from fastapi import APIRouter

user_routes = APIRouter()

@user_routes.get("/users")
async def get_users():
    return {"message": "User route works"}