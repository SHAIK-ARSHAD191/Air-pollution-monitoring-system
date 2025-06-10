from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SensorDataBase(BaseModel):
    location: str = Field(..., description="Location of the sensor")
    pm25: float = Field(..., description="PM2.5 concentration in μg/m³", ge=0)
    pm10: float = Field(..., description="PM10 concentration in μg/m³", ge=0)
    co2: float = Field(..., description="CO2 concentration in ppm", ge=0)
    co: float = Field(..., description="CO concentration in ppm", ge=0)
    temperature: float = Field(..., description="Temperature in °C")
    humidity: float = Field(..., description="Humidity percentage", ge=0, le=100)

class SensorDataCreate(SensorDataBase):
    pass

class SensorData(SensorDataBase):
    id: int
    timestamp: datetime
    aqi: Optional[int] = Field(None, description="Calculated Air Quality Index")

    class Config:
        from_attributes = True 