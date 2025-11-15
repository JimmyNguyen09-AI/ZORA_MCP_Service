from typing import List, Optional
from pydantic import BaseModel


class WeatherResponse(BaseModel):
    success: bool
    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    weather_code: int
    emoji: str


class TimeResponse(BaseModel):
    success: bool
    country: str
    timezone: str
    current_time: str
    date: str
    timestamp: str


class OwnerInfoResponse(BaseModel):
    success: bool
    name: str
    phone: str
    email: str
    role: str
    bio: str
    skills: List[str]


class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    detail: Optional[str] = None
