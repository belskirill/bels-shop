import datetime

from pydantic import BaseModel, ConfigDict

from src.schemas.users_auth import UserDTO, UserReviewDTO


class ReviewsDTO(BaseModel):
    id: int
    user_id: int
    goods_id: int
    datetime: datetime.datetime
    grade: int
    text: str


class ReviewsGetDTO(BaseModel):
    id: int
    user: UserReviewDTO
    goods_id: int
    datetime: datetime.datetime
    grade: int
    text: str

    model_config = ConfigDict(from_attributes=True)
