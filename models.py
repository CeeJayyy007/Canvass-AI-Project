from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from database import Base

# create sqlalchemy model from base for the creation of table 
class Status(Base):
    __tablename__ = "statusues"

    id = Column(Integer, primary_key=True, index=True)
    deviceId = Column(String(255), unique=True, nullable=False, index=True)
    timestamp = Column(
        DateTime, default=datetime.datetime.utcnow, nullable=False)
    pressure = Column(Integer)
    status = Column(String(10), default="OFF")
    temperature = Column(Integer)
