from typing import Annotated, Any, cast
from dataclasses import dataclass

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.api.core.utils.auth_utils import decode_jwt

from src.db.models import User, StaffMember
from src.db.utils.enums import Role

from src.core.config import redis


@dataclass
class AuthenticatedUser:
    model: User
    payload: dict[str, Any]


async def auth_by_token(
    access_token: HTTPAuthorizationCredentials = Depends(HTTPBearer())
) -> AuthenticatedUser:
    payload = decode_jwt(access_token.credentials)
    if payload is None:
        raise HTTPException(401, "Unauthorized (sign exp)")
    
    user_id: str = payload["sub"]
    token_status: bytes | None = await redis.get(f"token:{payload['jti']}:{user_id}")
    
    if token_status and token_status.decode() != "alive":
        raise HTTPException(401, "Token revoked (logout)")
    
    user = await User.filter(id=int(user_id) or None).first()
    if user and user.is_active:
        return AuthenticatedUser(model=user, payload=payload)

    raise HTTPException(401, "Unauthorized (user not found)")


async def check_is_staff_employee(user: AuthenticatedUser = Depends(auth_by_token)) -> StaffMember:
    await user.model.fetch_related("staff_member")
    staff_member = cast(StaffMember | None, user.model.staff_member)
    
    if staff_member:
        return staff_member
    raise HTTPException(403, "Forbidden (no staff member)")


async def check_is_staff_admin(
    staff_member: StaffMember = Depends(check_is_staff_employee)
) -> StaffMember:
    if staff_member.role.has_permission(Role.ADMIN, operator="ge"):
        return staff_member
    raise HTTPException(403, "Forbidden (no staff admin)")


AuthUser = Annotated[AuthenticatedUser, Depends(auth_by_token)]
StaffEmployee = Annotated[StaffMember, Depends(check_is_staff_employee)]
StaffAdmin = Annotated[StaffMember, Depends(check_is_staff_admin)]