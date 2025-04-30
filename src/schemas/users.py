from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.models.shops import ShopsOrm
from src.models.subscriptions import SubscriptionsOrm
from src.schemas.shop import ShopBase
from src.schemas.subscription import SubscriptionBase
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






class UserBase(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    number_phone: Optional[str]
    link_photo: Optional[str]
    about_me: Optional[str]
    shop: Optional[ShopBase]
    subscription: Optional[SubscriptionBase]

    model_config = ConfigDict(from_attributes=True)