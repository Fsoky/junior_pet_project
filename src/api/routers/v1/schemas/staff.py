from __future__ import annotations
from typing import Literal

from pydantic import BaseModel
from fastapi import Form

from src.db.utils.enums import Role


class AddNewEmployeeSchema(BaseModel):
    user_id: str
    role: Role
    
    @classmethod
    def as_form(cls, user_id: str = Form(...), role: Role = Form(...)) -> AddNewEmployeeSchema:
        return cls(user_id=user_id, role=role)


class UpdateEmployeeSchema(BaseModel):
    role: Role | None

    @classmethod
    def as_form(cls, role: Role | None = Form(None)) -> UpdateEmployeeSchema:
        return cls(role=role)