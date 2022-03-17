from typing import Optional
from sqlalchemy.orm import Session

import models
import schemas

# create crud functions to serve as utility functions

# create device status utility function
def create_device_status(db: Session, status: schemas.StatusCreate, deviceId: str):
    db_status = models.Status(**status.dict(), deviceId=deviceId)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

# get device to check if device exists 
def get_device(db: Session, deviceId: str):
    return db.query(models.Status).filter(models.Status.deviceId == deviceId).first()

# get all device statuses
def get_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()

# get histogram of status
def get_status_histogram(statuses, deviceId):
    histogram = {}

    for status in statuses:

        if status.status == "ON" and status.deviceId == deviceId:
            histogram["ON"] = histogram.get("ON", 0) + 1
        elif status.status == "OFF" and status.deviceId == deviceId:
            histogram["OFF"] = histogram.get("OFF", 0) + 1
        elif status.status == "ACTIVE" and status.deviceId == deviceId:
            histogram["ACTIVE"] = histogram.get("ACTIVE", 0) + 1
        elif status.status == "INACTIVE" and status.deviceId == deviceId:
            histogram["INACTIVE"] = histogram.get("INACTIVE", 0) + 1

    return histogram
