from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db_session
from app.schemas.inspection import InspectionCreate, InspectionRead
from app.services import inspection_service

router = APIRouter()


def _get_inspection_or_404(db: Session, inspection_id: str):
    inspection = inspection_service.get_inspection(db, inspection_id)
    if inspection is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Проверка не найдена")
    return inspection


@router.post(
    "/",
    response_model=InspectionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Создание проверки",
    description="Создает проверку и устанавливает статус 'ожидает отчет'",
)
def create_inspection(payload: InspectionCreate, db: Session = Depends(get_db_session)) -> InspectionRead:
    inspection = inspection_service.create_inspection(db, report_id=payload.report_id)
    return inspection_service.serialize_inspection(inspection)


@router.get(
    "/{inspection_id}",
    response_model=InspectionRead,
    summary="Получение проверки",
    description="Возвращает данные проверки",
)
def get_inspection(inspection_id: str, db: Session = Depends(get_db_session)) -> InspectionRead:
    inspection = _get_inspection_or_404(db, inspection_id)
    return inspection_service.serialize_inspection(inspection)