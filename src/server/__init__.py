# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings
from pathlib import Path as _Path
from typing import Optional


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

    API_HOST: str
    API_PORT: int
    API_RELOAD: bool

    SUPABASE_URL: str
    SUPABASE_KEY: str

    PG_USER: Optional[str] = None
    PG_PASS: Optional[str] = None
    PG_HOST: Optional[str] = None
    PG_PORT: Optional[str] = None
    PG_NAME: Optional[str] = None

    @property
    def PG_URL(self) -> Optional[str]:
        if all([self.PG_USER, self.PG_PASS, self.PG_HOST, self.PG_PORT, self.PG_NAME]):
            return f"postgresql://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"
        return None


settings = _Settings()
