from fastapi import APIRouter
from app.schemas import UserCreate
from app.services import create_user

router = APIRouter()

@router.post("/")
def create_user_route(user: UserCreate):
    user_id = create_user(user)
    return {"id": user_id}