from fastapi import APIRouter

router = APIRouter()

@router.get("/users/test")
def test_user():
    return {"message": "User route working!"}