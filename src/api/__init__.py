from fastapi import APIRouter

from .routers.v1 import setup_v1_routers


def setup_routers() -> APIRouter:
    router = APIRouter(prefix="/api")
    
    router.include_router(setup_v1_routers())
    return router