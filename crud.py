from typing import Optional
from sqlalchemy.orm import Session

import models
import schemas

# create crud functions to serve as utility functions

def create_device_status(db: Session, status: schemas.StatusCreate, deviceId: str):
    db_status = models.Status(**status.dict(), deviceId=deviceId)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_status(db: Session, device_id: int):
    return db.query(models.Status).filter(models.Status.owner_id == device_id).order_by(models.Status.id.desc()).first()




