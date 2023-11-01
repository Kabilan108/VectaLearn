# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings


class _Settings(_BaseSettings):
    """Server settings."""

    OPENAI_API_KEY: str
    HELICONE_API_KEY: str

    WHISPER_MODEL: str


settings = _Settings()
