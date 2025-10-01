import uuid

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

INSPECTION_STATUSES = (
    "booking",
    "check_in",
    "awaiting_report",
    "report_review",
    "completed",
)


class Inspection(Base):
    __tablename__ = "inspections"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    report_id = Column(String, ForeignKey("reports.id", ondelete="SET NULL"), nullable=True, index=True)
    status = Column(
        Enum(*INSPECTION_STATUSES, name="inspection_status"),
        nullable=False,
        default="awaiting_report",
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    report = relationship("Report", back_populates="inspection")