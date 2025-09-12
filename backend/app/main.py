from fastapi import FastAPI
from .api import endpoints

# Create FastAPI app instance
app = FastAPI(
    title="Autonomous Call Center",
    description="Backend for the Autonomous Call Center Management System",
    version="0.1.0",
)

# Include API routers
app.include_router(endpoints.router)

@app.get("/", tags=["Health Check"])
async def read_root():
    """Health check endpoint to confirm the server is running."""
    return {"status": "ok"}

# In a real application, you would also initialize database connections,
# logging, and other core services here.
# For example:
# from .core.config import settings
# from .services.database_client import db
#
# @app.on_event("startup")
# async def startup_event():
#     await db.connect(settings.MONGO_URI)
#
# @app.on_event("shutdown")
# async def shutdown_event():
#     await db.disconnect()
