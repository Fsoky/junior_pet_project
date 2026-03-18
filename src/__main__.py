from typing import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from tortoise import Tortoise
from pydantic import ValidationError
import uvicorn

from src.api import setup_routers
from src.core.config import config, TORTOISE_ORM


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await Tortoise.init(TORTOISE_ORM)
    
    try:
        yield
    finally:
        await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)
app.include_router(setup_routers())


@app.exception_handler(ValidationError)
def validation_error_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"msg": "Validation error", "error": [e["msg"] for e in exc.errors()]}
    )


if __name__ == "__main__":
    uvicorn.run("src.__main__:app", host=config.APP_HOST, port=config.APP_PORT, reload=True)