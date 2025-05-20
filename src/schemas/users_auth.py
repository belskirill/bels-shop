from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field, ConfigDict




class UserRequestDTO(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=6, max_length=24)


class UserAdd(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str


class UserAfterDTO(UserRequestDTO):
    shop_id: int
    link_photo: str
    number_phone: str
    about_me: str
    subscription_id: int


class UserDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    shop_id: Optional[int] = None
    link_photo: Optional[str] = None
    number_phone: Optional[str] = None
    about_me: Optional[str] = None
    subscription_id: Optional[int] = None

    # password_change_tokens: Optional[List[UserPasswordChache]]

    model_config = ConfigDict(from_attributes=True)


class UserInfoPatch(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    number_phone: Optional[str] = None
    about_me: Optional[str] = None


class UserEditDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    number_phone: str
    about_me: str

    # password_change_tokens: Optional[List[UserPasswordChache]]

    model_config = ConfigDict(from_attributes=True)


class UserReviewDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    link_photo: Optional[str] = None

    # password_change_tokens: Optional[List[UserPasswordChache]]

    model_config = ConfigDict(from_attributes=True)