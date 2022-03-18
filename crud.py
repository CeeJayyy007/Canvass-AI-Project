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
    return db.query(models.Status).filter(models.Status.deviceId == deviceId)

# get all device statuses


# get histogram of status


def get_status_histogram(statuses):

    # create dictionary to store histogram data
    histogram = {}

    # loop through status
    for status in statuses:

        # check each status object for status and deviceId
        if status.status == "ON":
            histogram["ON"] = histogram.get("ON", 0) + 1
        elif status.status == "OFF":
            histogram["OFF"] = histogram.get("OFF", 0) + 1
        elif status.status == "ACTIVE":
            histogram["ACTIVE"] = histogram.get("ACTIVE", 0) + 1
        elif status.status == "INACTIVE":
            histogram["INACTIVE"] = histogram.get("INACTIVE", 0) + 1

    return histogram
