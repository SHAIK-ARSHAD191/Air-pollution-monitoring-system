from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from .base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String, index=True)
    
    # Air quality parameters
    pm25 = Column(Float)  # PM2.5 in μg/m³
    pm10 = Column(Float)  # PM10 in μg/m³
    co2 = Column(Float)   # CO2 in ppm
    co = Column(Float)    # CO in ppm
    temperature = Column(Float)  # Temperature in °C
    humidity = Column(Float)     # Humidity in %
    
    # Air Quality Index calculation
    aqi = Column(Integer)  # Calculated Air Quality Index 