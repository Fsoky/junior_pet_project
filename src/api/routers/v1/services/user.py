import bcrypt
from typing import Any
from datetime import datetime, timezone

from src.api.core.base_service import BaseService, ServiceResponse
from src.api.core.utils import auth_utils

from src.api.routers.v1.schemas import (
    UserReigstrationSchema,
    UserLoginSchema,
    UpdateUserSchema
)


from src.db.models import User
from src.db.schemas import UserSchema

from src.core.config import redis


class UserService(BaseService):
    
    async def get_user(self, user: User) -> ServiceResponse:
        user_obj = (
            await UserSchema.from_tortoise_orm(user)
        ).model_dump(mode="json", exclude={"created_at", "updated_at"})
        return self.ok(user_obj)
    
    async def update_user(self, user: User, schema: UpdateUserSchema) -> ServiceResponse:
        user.update_from_dict(
            schema.model_dump(exclude_unset=True, exclude_none=True)
        )
        await user.save()
        
        return self.ok(message="User successfully updated")

    async def delete_user(self, user: User) -> ServiceResponse:
        user.is_active = False
        await user.save()
        
        return self.ok(message="User successfully deleted")

    async def register(self, schema: UserReigstrationSchema) -> ServiceResponse:
        user_exists = await User.filter(email__iexact=schema.email).exists()
        if user_exists:
            return self.error("User with same email already exists")
        
        hashed_password = bcrypt.hashpw(schema.password.encode(), bcrypt.gensalt())
        updated_schema = schema.model_copy(update={"password": hashed_password.decode()})
        
        await User.create(**updated_schema.model_dump())
        return self.ok(message="User successfully created")

    async def login(self, schema: UserLoginSchema) -> ServiceResponse:
        user = await User.filter(email=schema.email).first()
        
        if not user:
            return self.error("Unauthorized (user not found)", status=401)
        if not user.is_active:
            return self.error("User inactive", status=403)
        if not bcrypt.checkpw(schema.password.encode(), user.password.encode()):
            return self.error("Invalid password", status=401)
        
        payload = {
            "sub": str(user.id),
            "surname": user.surname,
            "middle_name": user.middle_name,
            "email": user.email
        }
        access_token = await auth_utils.encode_jwt(payload)
        
        return self.ok({"access_token": access_token})
    
    async def logout(self, payload: dict[str, Any]) -> ServiceResponse:
        now = datetime.now(timezone.utc)
        expire = datetime.fromtimestamp(payload["exp"], tz=timezone.utc)
        ttl = int((expire - now).total_seconds())
        
        await redis.set(f"token:{payload['jti']}:{payload['sub']}", "dead", ttl)
        return self.ok(message="Successfully logout")