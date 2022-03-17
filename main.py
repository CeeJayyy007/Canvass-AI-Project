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


# create FastAPI path operation code
@app.post("/devices/{deviceId}/status/", response_model=schemas.Status, status_code=status.HTTP_201_CREATED)
async def create_device_status(
    deviceId: str, db_status: schemas.StatusCreate, db: Session = Depends(get_db)
):

    # code commnunicates with function defined in crud.py file and returns a response
    return crud.create_device_status(db=db, status=db_status, deviceId=deviceId)


