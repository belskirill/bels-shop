import datetime

from pydantic import BaseModel


class ReviewsDTO(BaseModel):
    id: int
    user_id: int
    goods_id: int
    datetime: datetime
    grade: int
    text: str
