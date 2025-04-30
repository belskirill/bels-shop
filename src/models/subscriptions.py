from datetime import datetime

from sqlalchemy import ForeignKey, Boolean, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.database import Base


class SubscriptionsOrm(Base):
    __tablename__ = 'subscriptions'

    id: Mapped[int] = mapped_column(primary_key=True)
    status_active: Mapped[bool] = mapped_column(Boolean)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime)
    tarifs_id: Mapped[int] = mapped_column(Integer, ForeignKey('tarifs.id'))


    tarif: Mapped["TarifsOrm"] = relationship("TarifsOrm", back_populates="subscriptions")


    users: Mapped[list["UsersOrm"]] = relationship("UsersOrm", back_populates="subscription")
