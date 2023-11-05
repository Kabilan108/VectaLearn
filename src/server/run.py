# src/server/run.py

import uvicorn

from . import settings
from .api.main import app


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
    )
