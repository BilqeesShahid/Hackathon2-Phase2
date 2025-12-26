"""Main FastAPI application for Phase II Todo Backend."""
from fastapi import FastAPI
from app.middleware.cors import add_cors_middleware
from app.db.init import init_db

# Create FastAPI application
app = FastAPI(
    title="Evolution of Todo API",
    description="REST API for Phase II Full-Stack Todo Application",
    version="1.0.0",
    contact={
        "name": "Phase II Development Team",
    },
)

# Add CORS middleware
add_cors_middleware(app)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    init_db()
    print("Application startup complete. Database initialized.")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/")
async def root():
    """Root endpoint - API welcome message."""
    return {
        "message": "Welcome to Evolution of Todo API",
        "title": "Evolution of Todo API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


# Import and include routers
from app.routers import tasks, auth
app.include_router(auth.router)
app.include_router(tasks.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
