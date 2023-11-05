# src/server/api/main.py

from fastapi import FastAPI
from .routes import document, user, chat


app = FastAPI()

app.include_router(document.router, prefix="/document", tags=["document"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
