from typing import List, Literal
from pydantic import BaseModel
from datetime import datetime


class StatusBase(BaseModel):
    pressure: int
    temperature: int
    status: Literal["ON", "OFF", "ACTIVE", "INACTIVE"]


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int
    deviceId: str
    timestamp: datetime

    class Config:
        orm_mode = True


class StatusHistogram(BaseModel):
    deviceId: str
    ON: int = 0
    OFF: int = 0
    ACTIVE: int = 0
    INACTIVE: int = 0

    class Config:
        orm_mode = True
