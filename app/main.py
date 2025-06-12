from fastapi import FastAPI
from app.routes.user_routes import user_routes
from app.routes.conversation_routes import conversation_routes
from app.routes.message_routes import message_routes

app = FastAPI()

app.include_router(user_routes)
app.include_router(conversation_routes)
app.include_router(message_routes)

@app.get("/")
def read_root():
    return {"message": "Backend is finally working!"}