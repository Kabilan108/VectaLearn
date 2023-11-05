# src/server/api/routes/users.py

from fastapi import APIRouter


router = APIRouter()


@router.post("/create")
def create_user():
    pass
