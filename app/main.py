from fastapi import FastAPI
from app.routes import user_routes, conversation_routes, message_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(conversation_routes.router)
app.include_router(message_routes.router)

@app.get("/")
def read_root():
    return {"message": "Backend working perfectly!"}