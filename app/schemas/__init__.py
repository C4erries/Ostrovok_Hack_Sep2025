"""Общие схемы, доступные остальной части приложения."""

from .application import (
    ApplicationBase,
    ApplicationCreate,
    ApplicationFilter,
    ApplicationRead,
    ApplicationStatusUpdate,
)
from .auth import Message, Token, TokenPayload
from .hotel import HotelBase, HotelCreate, HotelRead, HotelUpdate
from .program_hotel import (
    ProgramHotelBase,
    ProgramHotelCreate,
    ProgramHotelRead,
    ProgramHotelUpdate,
)
from .user import UserBase, UserCreate, UserLogin, UserRead, UserUpdate

__all__ = [
    "ApplicationBase",
    "ApplicationCreate",
    "ApplicationFilter",
    "ApplicationRead",
    "ApplicationStatusUpdate",
    "Message",
    "Token",
    "TokenPayload",
    "HotelBase",
    "HotelCreate",
    "HotelRead",
    "HotelUpdate",
    "ProgramHotelBase",
    "ProgramHotelCreate",
    "ProgramHotelRead",
    "ProgramHotelUpdate",
    "UserBase",
    "UserCreate",
    "UserLogin",
    "UserRead",
    "UserUpdate",
]
