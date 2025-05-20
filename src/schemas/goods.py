from typing import Optional

from pydantic import BaseModel


class GoodsDTO(BaseModel):
    id: int
    name: str
    link_photo: Optional[str] = None
    price_one: int
    about: Optional[str] = None
    grade: Optional[int] = None
    shop_id: int
    count: int

class GoodsCreateDTO(BaseModel):
    name: str
    price_one: int
    about: str
    shop_id: int
    count: int