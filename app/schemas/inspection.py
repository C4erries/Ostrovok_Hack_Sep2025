from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class InspectionStatus(str, Enum):
    BOOKING = "booking"
    CHECK_IN = "check_in"
    AWAITING_REPORT = "awaiting_report"
    REPORT_REVIEW = "report_review"
    COMPLETED = "completed"


class InspectionCreate(BaseModel):
    report_id: str | None = Field(default=None)


class InspectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    report_id: str | None = None
    status: InspectionStatus
    created_at: datetime
    updated_at: datetime