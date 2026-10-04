# Import the Base class so SQLAlchemy knows about our model metadata.
from app.models.base import Base

# Import our database models so they can be registered with the application.
from app.models.url import URL
from app.models.user import User


# Defines what is available when this package is imported.
__all__ = ["Base", "User", "URL"]