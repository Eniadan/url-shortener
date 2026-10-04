from datetime import datetime
from typing import TYPE_CHECKING

# Import User for type checking without creating a circular import.
if TYPE_CHECKING:
    from app.models.user import User

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class URL(Base):
    # This tells SQLAlchemy that this class represents the "urls" table.
    __tablename__ = "urls"

    # Unique ID for each shortened URL.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Stores the original long URL that we want to shorten.
    original_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Stores the short code that users will use to access the URL.
    # It must be unique because two URLs cannot have the same short code.
    short_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False,
    )

    # Connects this URL to the user who created it.
    # The value must match an existing users.id.
        # Stores the ID of the user who created this shortened URL.
    #
    # ForeignKey makes sure this ID refers to a real user
    # in the "users" table.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # Gives us access to the User object that owns this URL.
    #
    # For example:
    # url.user.email
    user: Mapped["User"] = relationship(
        back_populates="urls",
    )

    # Keeps track of how many times this short URL has been visited.
    # New URLs start with zero clicks.
    click_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    # Allows us to disable a short URL without deleting it from the database.
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # Records when the URL was created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    # Records when the URL was last updated.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )