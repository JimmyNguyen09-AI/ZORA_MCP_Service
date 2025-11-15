"""
API routers for ZORA MCP Service.
"""

from .routes_root import router as root_router
from .routes_weather import router as weather_router
from .routes_time import router as time_router
from .routes_owner import router as owner_router
from .routes_tools import router as tools_router

__all__ = [
    "root_router",
    "weather_router",
    "time_router",
    "owner_router",
    "tools_router",
]
