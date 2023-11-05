# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings
import streamlit as _st

from client.schema import Session as _Session


class _Settings(_BaseSettings):
    """Client settings."""

    STREAMLIT_DEBUG: bool

    API_BASE: str

    SUPABASE_URL: str
    SUPABASE_KEY: str

    def get_endpoint(self, endpoint: str) -> str:
        """Get the full endpoint URL."""

        return f"{self.API_BASE}{endpoint}"


settings = _Settings()


def get_user() -> _Session:
    """Get the user ID from the session state."""
    return _Session(
        user_id=_st.session_state.get("user_id", ""),
        jwt=_st.session_state.get("jwt", ""),
    )


def set_user(user_id: str, token: str) -> None:
    """Set the user ID in the session state."""
    _st.session_state["user_id"] = user_id
    _st.session_state["jwt"] = token
