# app/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings


class _Settings(_BaseSettings):
    OPENAI_API_KEY: str
    HELICONE_API_KEY: str


settings = _Settings()
