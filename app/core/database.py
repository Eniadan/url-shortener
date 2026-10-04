from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# Create the connection between SQLAlchemy and PostgreSQL.
engine = create_engine(
    settings.database_url,
)


# Creates database sessions that our API will use to talk to PostgreSQL.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db():
    # Create a new database session for this request.
    db = SessionLocal()

    try:
        # Make the session available to the API endpoint.
        yield db
    finally:
        # Always close the session to release database resources.
        db.close()