from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import *

import os
PORT = os.getenv("PORT",8001)
app = FastAPI(
    title="ZORA MCP Service",
    description="Model Context Protocol Service for ZORA AI - Weather, Time & Owner Info",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root_router)
app.include_router(weather_router, prefix="/api", tags=["weather"])
app.include_router(time_router, prefix="/api", tags=["time"])
app.include_router(owner_router, prefix="/api", tags=["owner"])
app.include_router(tools_router, prefix="/api", tags=["tools"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=PORT,
        reload=True
    )
    # uvicorn.run(
    #     "app.main:app",
    #     host="0.0.0.0",
    #     port=PORT,
    #     reload=True
    # )
