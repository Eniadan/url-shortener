from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.url import URL


class User(Base):
    # Each User object represents a row in the "users" table.
    __tablename__ = "users"

    # Unique identifier for the user.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Used when the user logs in.
    # The unique constraint prevents two accounts from using the same email.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    # We store a hashed password instead of the user's actual password.
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Records when the account was created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    # Records when the account information was last updated.
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    # One user can create many shortened URLs.
    #
    # This gives us access to a user's URLs through:
    # user.urls
    urls: Mapped[list["URL"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )