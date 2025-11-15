from datetime import datetime
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "service": "ZORA MCP Service",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "weather": "/api/weather?city={city}",
            "time": "/api/time?country={country}",
            "owner": "/api/owner",
            "tools": "/api/tools",
        },
    }


@router.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
