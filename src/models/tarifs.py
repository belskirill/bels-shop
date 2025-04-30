

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class TarifsOrm(Base):
    __tablename__ = 'tarifs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    subscriptions: Mapped[list["SubscriptionsOrm"]] = relationship("SubscriptionsOrm", back_populates="tarif")
