from typing import Optional

from pydantic import BaseModel, ConfigDict


class ShopBaseDTO(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None
    link_photo: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    status_open: Optional[bool] = None
    user_id: Optional[int] = None
    confirmed: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class ShopAddDTO(BaseModel):
    name: str
    description: str
    address: str
    phone: str



class ShopUpdateDTO(BaseModel):
    name: str
    description: str
    address: str
    phone: str
    user_id: int

class ShopPatchDTO(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None


