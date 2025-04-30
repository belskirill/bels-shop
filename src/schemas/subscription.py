from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.schemas.tarifs import TarifBase


class SubscriptionBase(BaseModel):
    id: int
    status_active: bool
    start_date: datetime
    end_date: datetime
    tarif: Optional[TarifBase]