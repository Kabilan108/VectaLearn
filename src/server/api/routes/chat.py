# src/server/api/routes/chat.py

from fastapi import APIRouter


router = APIRouter()


@router.post("/send")
def send_message():
    pass
