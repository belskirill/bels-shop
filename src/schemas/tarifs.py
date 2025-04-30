from pydantic import BaseModel


class TarifBase(BaseModel):
    id: int
    name: str