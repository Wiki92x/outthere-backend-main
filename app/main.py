from fastapi import FastAPI
from routes.user_routes import user_routes
from routes.conversation_routes import conversation_routes
from routes.message_routes import message_routes

app = FastAPI()

app.include_router(user_routes)
app.include_router(conversation_routes)
app.include_router(message_routes)

@app.get("/")
def health_check():
    return {"message": "Backend is running!"}