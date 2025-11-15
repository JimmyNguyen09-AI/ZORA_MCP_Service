from fastapi import APIRouter

from app.models import WeatherResponse
from app.services import WeatherService


router = APIRouter()
weather_service = WeatherService()


@router.get("/weather", response_model=WeatherResponse)
async def get_weather(city: str):
    """
    Get current weather for a Vietnamese city
    """
    return await weather_service.get_weather(city)
