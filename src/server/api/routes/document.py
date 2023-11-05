# src/server/api/routes/document.py

from fastapi import APIRouter


router = APIRouter()


@router.post("/upload")
def upload_document():
    pass
