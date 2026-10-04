
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


# Defines the data a new user must provide to register.
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


# Defines the user information returned by the API.
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # Allows Pydantic to read data directly from SQLAlchemy objects.
    model_config = ConfigDict(from_attributes=True)
