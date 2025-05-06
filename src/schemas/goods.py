from pydantic import BaseModel


class GoodsDTO(BaseModel):
    id: int
    name: str
    link_photo: str
    price_one: int
    about: str
    grade: int
    shop_id: int
    count: int