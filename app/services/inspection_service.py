from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.inspection import Inspection
from app.models.report import Report
from app.schemas.inspection import InspectionRead


def create_inspection(db: Session, *, report_id: str | None = None) -> Inspection:
    inspection = Inspection(report_id=report_id)

    if report_id:
        report = db.get(Report, report_id)
        if report is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Отчет не найден")
        inspection.report = report

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
            "report_id": inspection.report_id,
            "status": inspection.status,
            "created_at": inspection.created_at,
            "updated_at": inspection.updated_at,
        }
    )