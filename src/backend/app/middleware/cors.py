"""CORS configuration for Next.js + FastAPI integration."""
from fastapi.middleware.cors import CORSMiddleware
import os

# Get allowed origins from environment
DEV_ORIGIN = os.environ.get("NEXT_PUBLIC_API_URL", "http://localhost:8000").replace("/api", "")

# List of allowed origins
ALLOWED_ORIGINS = [
    DEV_ORIGIN,  # http://localhost:3000
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Add production frontend URL here when deploying
    # "https://your-production-domain.com",
]


def add_cors_middleware(app):
    """Add CORS middleware to the FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
