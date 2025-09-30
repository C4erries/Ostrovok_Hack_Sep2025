from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HotelBase(BaseModel):
    """Базовая информация об отеле, используемая при создании и обновлении."""

    name: str
    city: str
    address: str
    rooms_total: int | None = None
    description: str | None = None
    is_active: bool = True


class HotelCreate(HotelBase):
    """Схема для добавления отеля в программу."""

    pass


class HotelUpdate(BaseModel):
    """Схема частичного обновления данных об отеле."""

    name: str | None = None
    city: str | None = None
    address: str | None = None
    rooms_total: int | None = None
    description: str | None = None
    is_active: bool | None = None


class HotelRead(HotelBase):
    """Схема для выдачи информации об отеле наружу."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
