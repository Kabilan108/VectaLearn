# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings


class _Settings(_BaseSettings):
    """Client settings."""

    STREAMLIT_DEBUG: bool


settings = _Settings()
