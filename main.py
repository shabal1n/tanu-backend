from fastapi import FastAPI

from app.api import routers
from app.core.config import settings

app = FastAPI()

app.include_router(routers, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        log_level=settings.LOG_LEVEL,
        reload=settings.DEBUG,
    )
