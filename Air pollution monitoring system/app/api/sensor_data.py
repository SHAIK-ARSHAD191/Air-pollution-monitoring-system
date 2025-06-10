from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ..schemas.sensor_data import SensorData, SensorDataCreate
from ..services.sensor_service import create_sensor_data, get_latest_readings, get_historical_data
from ..models.base import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sensor-data/", response_model=SensorData)
def add_sensor_data(data: SensorDataCreate, db: Session = Depends(get_db)):
    """Add new sensor data reading"""
    return create_sensor_data(db, data)

@router.get("/sensor-data/latest/", response_model=List[SensorData])
def read_latest_data(location: str = None, db: Session = Depends(get_db)):
    """Get latest sensor readings"""
    return get_latest_readings(db, location)

@router.get("/sensor-data/historical/", response_model=List[SensorData])
def read_historical_data(
    location: str = None,
    start_time: datetime = None,
    end_time: datetime = None,
    db: Session = Depends(get_db)
):
    """Get historical sensor data"""
    return get_historical_data(db, location, start_time, end_time) 