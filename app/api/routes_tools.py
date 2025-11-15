from fastapi import APIRouter

from app.core import VIETNAM_CITIES, COUNTRY_TIMEZONES


router = APIRouter()


@router.get("/tools")
def get_available_tools():
    """
    Get list of available MCP tools
    """
    return {
        "tools": [
            {
                "name": "get_weather",
                "endpoint": "/api/weather",
                "method": "GET",
                "description": "Lấy thông tin thời tiết hiện tại của một thành phố ở Việt Nam",
                "parameters": {
                    "city": {
                        "type": "string",
                        "required": True,
                        "description": "Tên thành phố (vd: Hanoi, Ho Chi Minh, Da Nang)",
                    }
                },
                "keywords": [
                    "thời tiết",
                    "nhiệt độ",
                    "nóng",
                    "lạnh",
                    "mưa",
                    "nắng",
                    "weather",
                    "temperature",
                    "hot",
                    "cold",
                    "rain",
                    "sunny",
                ],
                "example": "GET /api/weather?city=Hanoi",
            },
            {
                "name": "get_time",
                "endpoint": "/api/time",
                "method": "GET",
                "description": "Lấy thời gian hiện tại của một quốc gia",
                "parameters": {
                    "country": {
                        "type": "string",
                        "required": True,
                        "description": "Tên quốc gia (vd: Vietnam, USA, Japan)",
                    }
                },
                "keywords": [
                    "mấy giờ",
                    "giờ",
                    "thời gian",
                    "múi giờ",
                    "bây giờ",
                    "what time",
                    "time",
                    "current time",
                    "timezone",
                    "clock",
                ],
                "example": "GET /api/time?country=Vietnam",
            },
            {
                "name": "get_owner_info",
                "endpoint": "/api/owner",
                "method": "GET",
                "description": "Lấy thông tin về người tạo ra ZORA AI",
                "parameters": {},
                "keywords": [
                    "ai tạo",
                    "người tạo",
                    "chủ nhân",
                    "developer",
                    "creator",
                    "who created",
                    "who made",
                    "owner",
                    "contact",
                ],
                "example": "GET /api/owner",
            },
        ],
        "cities": list(set([name for name, _, _ in VIETNAM_CITIES.values()])),
        "countries": list(COUNTRY_TIMEZONES.keys()),
    }
