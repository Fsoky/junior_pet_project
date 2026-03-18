"""mypy будет ругаться на методы в классе (tortoise-orm принимает strEnum)
other: Role можно поменять на str или написать метод has_permissions(...)
и не использовать magic-методы
"""

from __future__ import annotations
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
    
    def __lt__(self, other: Role) -> bool:
        if not isinstance(other, Role):
            return NotImplemented
        return _order[self.value] < _order[other.value]
    
    def __gt__(self, other: Role) -> bool:
        if not isinstance(other, Role):
            return NotImplemented
        return _order[self.value] > _order[other.value]
    
    def __le__(self, other: Role) -> bool:
        return self < other or self == other
    
    def __ge__(self, other: Role) -> bool:
        return self > other or self == other