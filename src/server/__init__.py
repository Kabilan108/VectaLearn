# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings
from pathlib import Path as _Path


_MODULE_PATH = _Path(__file__).resolve().parent
_ROOT_PATH = _MODULE_PATH.parent.parent


class _Settings(_BaseSettings):
    """Server settings."""

    PROJECT_NAME: str

    OPENAI_API_KEY: str
    HELICONE_API_KEY: str

    WHISPER_MODEL: str

    ROOT_PATH: str = _ROOT_PATH.as_posix()
    MODULE_PATH: str = _MODULE_PATH.as_posix()
    MODEL_PATH: str = _ROOT_PATH.joinpath("models").as_posix()


settings = _Settings()
