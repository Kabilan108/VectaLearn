# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings

from pathlib import Path
import os


MODULE_PATH = Path(os.path.dirname(os.path.abspath(__file__))).parent


class _Settings(_BaseSettings):
    """Server settings."""

    OPENAI_API_KEY: str

    WHISPER_MODEL: str

    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str


settings = _Settings()
