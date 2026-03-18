from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.api.core.dependencies import AuthUser

from src.api.routers.v1.services import UserService
from src.api.routers.v1.schemas import (
    UserReigstrationSchema,
    UserLoginSchema,
    UpdateUserSchema
)

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()


@router.get("")
async def get_user(user: AuthUser) -> JSONResponse:
    res = await service.get_user(user.model)
    return JSONResponse(**res.response())


@router.put("")
async def update_user(
    user: AuthUser,
    schema: UpdateUserSchema = Depends(UpdateUserSchema.as_form),
) -> JSONResponse:
    res = await service.update_user(user.model, schema)
    return JSONResponse(**res.response())


@router.delete("")
async def delete_user(user: AuthUser) -> JSONResponse:
    res = await service.delete_user(user.model)
    return JSONResponse(**res.response())


@router.post("/auth/register")
async def register(
    schema: UserReigstrationSchema = Depends(UserReigstrationSchema.as_form)
) -> JSONResponse:
    res = await service.register(schema)
    return JSONResponse(**res.response())


@router.post("/auth/login")
async def login(schema: UserLoginSchema = Depends(UserLoginSchema.as_form)) -> JSONResponse:
    res = await service.login(schema)
    return JSONResponse(**res.response())


@router.post("/auth/logout")
async def logout(user: AuthUser) -> JSONResponse:    
    res = await service.logout(user.payload)
    return JSONResponse(**res.response())