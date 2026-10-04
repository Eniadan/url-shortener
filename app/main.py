
from fastapi import FastAPI
from app.api.routes.users import router as users_router

from app.api.routes.health import router as health_router


app = FastAPI(
    title="URL Shortener API",
)


# Register the health-check endpoints with the application.
app.include_router(health_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}
