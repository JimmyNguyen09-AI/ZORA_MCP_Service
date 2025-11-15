from fastapi import HTTPException
import httpx

from app.core import VIETNAM_CITIES, WEATHER_CODES
from app.core import get_weather_emoji
from app.models import WeatherResponse


class WeatherService:
    """
    Service xử lý logic lấy thời tiết từ Open-Meteo
    """
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    async def get_weather(self, city: str) -> WeatherResponse:
        city_normalized = city.lower().strip()
        city_data = VIETNAM_CITIES.get(city_normalized)
        if not city_data:
            raise HTTPException(
                status_code=404,
                detail=(
                    f"City '{city}' not found. "
                    "Supported cities: Hanoi, Ho Chi Minh, Da Nang, Hue, etc."
                ),
            )
        city_name, lat, lon = city_data
        try:
            async with httpx.AsyncClient() as client:
                params = {
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                    "timezone": "Asia/Bangkok",
                }

                response = await client.get(self.BASE_URL, params=params, timeout=10.0)
                response.raise_for_status()
                data = response.json()

                current = data["current"]
                weather_code = current.get("weather_code", 0)
                description = WEATHER_CODES.get(weather_code, "Không xác định")
                emoji = get_weather_emoji(weather_code)

                return WeatherResponse(
                    success=True,
                    city=city_name,
                    temperature=current["temperature_2m"],
                    description=description,
                    humidity=current["relative_humidity_2m"],
                    wind_speed=current["wind_speed_10m"],
                    weather_code=weather_code,
                    emoji=emoji,
                )

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Weather service error: {str(e)}")
