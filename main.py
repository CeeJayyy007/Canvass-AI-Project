from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

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
async def status_histogram(deviceId: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    db_device = crud.get_device(db, deviceId=deviceId)

    if db_device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found")

    statuses = crud.get_statuses(db, skip = skip, limit=limit)

    status_histogram = crud.get_status_histogram(statuses, deviceId)

    return {**status_histogram, "deviceId": db_device.deviceId}
