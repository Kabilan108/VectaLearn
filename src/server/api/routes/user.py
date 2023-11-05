# src/server/api/routes/users.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from ...schema.user import User, NewUser, AuthResponse
from .. import supabase


router = APIRouter()
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/signup", response_model=AuthResponse)
async def sign_up(user: NewUser):
    """Sign up a new user."""

    try:
        res = supabase.auth.sign_up(user.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error signing up user: " + str(e))

    return {
        "message": "User created successfully!",
        "user_id": res.user.id,
        "jwt": res.session.access_token,
    }


@router.post("/login", response_model=AuthResponse)
async def log_in(user: User):
    """Log in an existing user."""

    try:
        res = supabase.auth.sign_in_with_password(user.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error logging in user: " + str(e))

    return {
        "message": "User logged in successfully!",
        "user_id": res.user.id,
        "jwt": res.session.access_token,
    }


@router.post("/logout")
async def log_out(token: str = Depends(ouath2_scheme)):
    """Log out the current user."""

    try:
        res = supabase.auth.sign_out(token)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error logging out user: " + str(e))

    return res


@router.get("/profile")
async def get_profile():
    pass


@router.put("/profile")
async def update_profile():
    pass


@router.post("/password/reset")
async def reset_password(email: str):
    pass
