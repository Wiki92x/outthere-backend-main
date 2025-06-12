from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, User
from app.services import user_service

user_routes = APIRouter()

@user_routes.post("/users")
def create_user(user: UserCreate):
    return user_service.create_user(user)