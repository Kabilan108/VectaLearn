# src/server/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import document, user, chat
from .. import settings

app = FastAPI()

origins = [
    settings.CLIENT_URL,  # Allow Streamlit app to access the server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(document.router, prefix="/document", tags=["document"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
