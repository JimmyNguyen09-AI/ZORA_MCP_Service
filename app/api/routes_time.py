from fastapi import APIRouter

from app.models import TimeResponse
from app.services import TimeService


router = APIRouter()
time_service = TimeService()


@router.get("/time", response_model=TimeResponse)
def get_time(country: str):
    """
    Get current time for a country
    """
    return time_service.get_time(country)
