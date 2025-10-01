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
    hotel_id: int = Field(gt=0)


class InspectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: int
    hotel_id: int
    report_id: str | None = None
    status: InspectionStatus
    created_at: datetime
    updated_at: datetime