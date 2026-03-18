from __future__ import annotations
from typing import Annotated
from annotated_types import MinLen, MaxLen

from pydantic import BaseModel, EmailStr, ValidationInfo, field_validator
from fastapi import Form


class BaseUserSchema(BaseModel):
    surname: Annotated[str | None, MinLen(1), MaxLen(64)]
    middle_name: Annotated[str | None, MinLen(2), MaxLen(64)]
    email: EmailStr | None
    password: Annotated[str | None, MinLen(3), MaxLen(64)]
    password_repeat: Annotated[str | None, MinLen(3), MaxLen(64)]

    @field_validator("password_repeat", mode="after")
    @classmethod
    def check_passwords_match(cls, value: str, info: ValidationInfo) -> str:
        if value is None or info.data["password"] is None:
            return value
        
        if value != info.data["password"]:
            raise ValueError("Password do not match!")
        return value


class UserReigstrationSchema(BaseUserSchema):
    surname: Annotated[str, MinLen(1), MaxLen(64)]
    middle_name: Annotated[str, MinLen(2), MaxLen(64)]
    email: EmailStr
    password: Annotated[str, MinLen(6), MaxLen(128)]
    password_repeat: Annotated[str, MinLen(6), MaxLen(128)]
    
    @classmethod
    def as_form(
        cls,
        surname: str = Form(...),
        middle_name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        password_repeat: str = Form(...)
    ) -> UserReigstrationSchema:
        return cls(
            surname=surname,
            middle_name=middle_name,
            email=email,
            password=password,
            password_repeat=password_repeat
        )


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    
    @classmethod
    def as_form(cls, email: str = Form(...), password: str = Form(...)) -> UserLoginSchema:
        return cls(email=email, password=password)


class UpdateUserSchema(BaseUserSchema):

    @classmethod
    def as_form(
        cls,
        surname: str | None = Form(None),
        middle_name: str | None = Form(None),
        email: str | None = Form(None),
        password: str | None = Form(None),
        password_repeat: str | None = Form(None)
    ) -> UpdateUserSchema:
        return cls(
            surname=surname,
            middle_name=middle_name,
            email=email,
            password=password,
            password_repeat=password_repeat
        )