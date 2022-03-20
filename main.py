from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import uvicorn

import crud
import models
import schemas
from database import SessionLocal, engine

# create database table
models.Base.metadata.create_all(bind=engine)

# initialize FastAPI
app = FastAPI()


# create Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create FastAPI path operation code for creating status of devices
@app.post("/devices/{deviceId}/status/", response_model=schemas.Status, status_code=status.HTTP_201_CREATED)
async def create_device_status(
    deviceId: str, db_status: schemas.StatusCreate, db: Session = Depends(get_db)
):

    # code commnunicates with function defined in crud.py file and returns a response
    return crud.create_device_status(db=db, status=db_status, deviceId=deviceId)


# create FastAPI path operation code for getting device status histagram
@app.get("/statuses/histogram/{deviceId}", response_model=schemas.StatusHistogram, status_code=status.HTTP_200_OK)
async def status_histogram(deviceId: str, db: Session = Depends(get_db)):

    # get records of specific deviceId from the database
    statuses = crud.get_device(db, deviceId=deviceId)

    # if records of selected deviceId exists
    if statuses.first():
        status_histogram = crud.get_status_histogram(statuses)

    # if records of selected deviceId does not exist
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")

    return {**status_histogram, "deviceId": deviceId}

# create FastAPI path operation code for getting devices with top parameters


@app.get("/devices/{parameter}", status_code=status.HTTP_200_OK)
async def get_parameter(parameter=str, db: Session = Depends(get_db)):

    db_parameter = crud.create_parameter_model(parameter)

    # get all status data from database session
    db_data = db.query(models.Status).order_by(
        db_parameter.desc())

    # limit db_data to only 10 entries
    db_data_top = db_data.limit(10).all()

    return db_data_top


# scheduler
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
