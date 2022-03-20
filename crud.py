from http.client import HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status

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
        if status.status == status.status:
            histogram[status.status] = histogram.get(status.status, 0) + 1

    return histogram

# API to return parameter as model


def create_parameter_model(parameter):

    # check if parameter sent is temperature
    if parameter == models.Status.temperature.key:

        db_parameter = models.Status.temperature

    # check if parameter sent is pressure
    elif parameter == models.Status.pressure.key:

        db_parameter = models.Status.pressure

    # if parameter does not match database parameters, then raise an exception
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Parameter does not exist")

    return db_parameter
