from __future__ import annotations
from typing import Literal
from enum import Enum

_order = {
    "employee": 1,
    "admin": 2,
    "superadmin": 3
}


class Role(str, Enum):
    """Role
    - employee - обычный сотрудник, без прав манипулирования данными (просмотр личной информации)
    - admin - назначение новых сотрудников
    - superadmin - назначение новых админов и сотрудников
    """
    
    EMPLOYEE = "employee"
    ADMIN = "admin"
    SUPERADMIN = "superadmin"
    
    def has_permission(
        self,
        role: Role,
        *,
        operator: Literal["gt", "lt", "ge", "le"] = "gt"
    ) -> bool:
        match operator:
            case "gt":
                return _order[self.value] > _order[role.value]
            case "lt":
                return _order[self.value] < _order[role.value]
            case "ge":
                return _order[self.value] >= _order[role.value]
            case "le":
                return _order[self.value] <= _order[role.value]
            case _:
                raise ValueError(f"Unknown operator ({operator})")