
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db


# Groups our health-check endpoints together.
router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/database")
def check_database(db: Session = Depends(get_db)):
    # Run a simple query to confirm PostgreSQL is responding.
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }
