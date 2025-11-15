from datetime import datetime
from fastapi import HTTPException
import pytz
from app.core import COUNTRY_TIMEZONES
from app.models import TimeResponse
class TimeService:
    """
    Service xử lý lấy thời gian theo quốc gia
    """

    def get_time(self, country: str) -> TimeResponse:
        country_normalized = country.lower().strip()
        timezone_str = COUNTRY_TIMEZONES.get(country_normalized)
        if not timezone_str:
            available = ", ".join(list(COUNTRY_TIMEZONES.keys())[:10])
            raise HTTPException(
                status_code=404,
                detail=f"Country '{country}' not found. Available: {available}, ...",
            )
        try:
            tz = pytz.timezone(timezone_str)
            current_time = datetime.now(tz)
            return TimeResponse(
                success=True,
                country=country.title(),
                timezone=timezone_str,
                current_time=current_time.strftime("%H:%M:%S"),
                date=current_time.strftime("%d/%m/%Y"),
                timestamp=current_time.isoformat(),
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Time service error: {str(e)}")
