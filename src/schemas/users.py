from pydantic import BaseModel, EmailStr, Field


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


class UserAfterDTO(UserRequestDTO):
    shop_id: int
    link_photo: str
    number_phone: str
    about_me: str
    subscription_id: int


class UserDTO(UserAfterDTO):
    id: int
