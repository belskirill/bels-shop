from pydantic import BaseModel


class ShopBase(BaseModel):
    id: int
    link_photo: str
    name: str
    address: str
    phone: str
    status_open: bool