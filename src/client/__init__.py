# src/client/__init__.py

from pydantic_settings import BaseSettings as _BaseSettings


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
