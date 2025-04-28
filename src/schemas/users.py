from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.schemas.users_auth import UserDTO


class UsersRequest(BaseModel):
    email: EmailStr
    old_password: str = Field(min_length=6, max_length=24)
    new_password: str = Field(min_length=6, max_length=24)


class UserPasswordChache(BaseModel):
    user_id: int
    token: str
    new_password_hash: str
    expires_at: datetime
    is_used: bool

    # user: Optional[UserDTO]


class UsersResponsePassword(UserPasswordChache):
    id: int

    model_config = ConfigDict(from_attributes=True)