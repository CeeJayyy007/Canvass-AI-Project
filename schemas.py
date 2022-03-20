from typing import Literal, Optional
from pydantic import BaseModel
from datetime import datetime

# create StatusBase model form pydantic base model


class StatusBase(BaseModel):
    pressure: int
    temperature: int
    status: Literal["ON", "OFF", "ACTIVE", "INACTIVE"]

# create StatusCreate model form pydantic StatusBase model with the consideration of shared attributes in mind


class StatusCreate(StatusBase):
    pass

# create Status model form pydantic StatusBase model with the consideration of shared attributes in mind


class Status(StatusBase):
    id: int
    deviceId: str
    timestamp: datetime

    class Config:
        orm_mode = True

# create StatusHistogram model form pydantic BaseModel


class StatusHistogram(BaseModel):
    deviceId: str
    ON: int = 0
    OFF: int = 0
    ACTIVE: int = 0
    INACTIVE: int = 0

    # include config class to provide configurations to pydantic
    class Config:
        orm_mode = True

# create StatusHistogram model form pydantic BaseModel


class TopParameters(BaseModel):
    deviceId: str
    temperature: Optional[int]
    pressure: Optional[int]

    # include config class to provide configurations to pydantic
    class Config:
        orm_mode = True
