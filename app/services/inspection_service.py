from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.inspection import Inspection
from app.models.report import Report
from app.models.user import User
from app.schemas.inspection import InspectionRead
from app.services import hotel_service, program_hotel_service


def create_inspection(db: Session, *, user: User, hotel_id: int) -> Inspection:
    hotel = hotel_service.get_hotel(db, hotel_id)
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Отель не найден")

    if not program_hotel_service.is_hotel_available_for_user(db, hotel_id=hotel_id, user=user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отель недоступен для пользователя",
        )

    inspection = Inspection(user_id=user.id, hotel_id=hotel_id)

    db.add(inspection)
    db.commit()
    db.refresh(inspection)
    return inspection


def get_inspection(db: Session, inspection_id: str) -> Inspection | None:
    return db.get(Inspection, inspection_id)


def serialize_inspection(inspection: Inspection) -> InspectionRead:
    return InspectionRead.model_validate(
        {
            "id": inspection.id,
            "user_id": inspection.user_id,
            "hotel_id": inspection.hotel_id,
            "report_id": inspection.report_id,
            "status": inspection.status,
            "created_at": inspection.created_at,
            "updated_at": inspection.updated_at,
        }
    )