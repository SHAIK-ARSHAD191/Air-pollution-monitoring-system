from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Optional
from ..models.sensor_data import SensorData
from ..schemas.sensor_data import SensorDataCreate

def calculate_aqi(pm25: float, pm10: float) -> int:
    """
    Calculate Air Quality Index based on PM2.5 and PM10 values
    Using a simplified version of the EPA AQI calculation
    """
    # PM2.5 breakpoints
    if pm25 <= 12.0:
        aqi = (50 - 0) * (pm25 - 0) / (12.0 - 0) + 0
    elif pm25 <= 35.4:
        aqi = (100 - 51) * (pm25 - 12.1) / (35.4 - 12.1) + 51
    elif pm25 <= 55.4:
        aqi = (150 - 101) * (pm25 - 35.5) / (55.4 - 35.5) + 101
    else:
        aqi = 151  # Unhealthy or worse

    return round(aqi)

def create_sensor_data(db: Session, data: SensorDataCreate) -> SensorData:
    """Create new sensor data entry"""
    aqi = calculate_aqi(data.pm25, data.pm10)
    db_data = SensorData(
        **data.model_dump(),
        aqi=aqi
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_latest_readings(db: Session, location: Optional[str] = None) -> List[SensorData]:
    """Get the latest sensor readings, optionally filtered by location"""
    query = db.query(SensorData)
    if location:
        query = query.filter(SensorData.location == location)
    return query.order_by(SensorData.timestamp.desc()).limit(10).all()

def get_historical_data(
    db: Session,
    location: Optional[str] = None,
    start_time: datetime = None,
    end_time: datetime = None
) -> List[SensorData]:
    """Get historical sensor data within a time range"""
    if not start_time:
        start_time = datetime.utcnow() - timedelta(days=7)
    if not end_time:
        end_time = datetime.utcnow()

    query = db.query(SensorData)
    if location:
        query = query.filter(SensorData.location == location)
    
    return query.filter(
        SensorData.timestamp.between(start_time, end_time)
    ).order_by(SensorData.timestamp.desc()).all() 