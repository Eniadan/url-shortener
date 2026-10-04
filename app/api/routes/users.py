
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


# Keeps all user-related endpoints together.
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    # Check whether someone has already registered with this email.
    existing_user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )

    # Hash the password before saving it.
    new_user = User(
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    # Add the new user to the current database transaction.
    db.add(new_user)

    try:
        # Save the user to PostgreSQL.
        db.commit()
    except IntegrityError:
        # Roll back if the database rejects the insert,
        # such as when another request registers the same email.
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )

    # Load database-generated values, such as the user's ID.
    db.refresh(new_user)

    return new_user
