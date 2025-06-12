from fastapi import FastAPI
from app.routes import user_routes, conversation_routes, message_routes

app = FastAPI()

app.include_router(user_routes, prefix="/users", tags=["Users"])
app.include_router(conversation_routes, prefix="/conversations", tags=["Conversations"])
app.include_router(message_routes, prefix="/messages", tags=["Messages"])

@app.get("/")
def read_root():
    return {"status": "Backend Phase 3 Ready"}