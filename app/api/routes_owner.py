from fastapi import APIRouter

from app.models import OwnerInfoResponse
from app.services import OwnerService


router = APIRouter()
owner_service = OwnerService()


@router.get("/owner", response_model=OwnerInfoResponse)
def get_owner():
    """
    Get information about ZORA AI's creator
    """
    return owner_service.get_owner_info()
