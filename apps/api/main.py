from fastapi import FastAPI

from apps.api.routers import health, profiles

app = FastAPI(
    title="CareerOS API",
    description="Open source career intelligence platform API",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(profiles.router)
