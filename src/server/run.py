# src/server/run.py

import uvicorn

from server import settings


if __name__ == "__main__":
    uvicorn.run(
        "server.api.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD,
    )
