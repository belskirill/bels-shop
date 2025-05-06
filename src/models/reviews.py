from sqlalchemy import String, Boolean, ForeignKey, Integer, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import datetime

from src.database import Base


class ReviewsOrm(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    goods_id: Mapped[int] = mapped_column(ForeignKey('goods.id'))
    datetime: Mapped[datetime] = mapped_column(DateTime)
    grade: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="reviews")
    goods: Mapped["GoodsOrm"] = relationship("GoodsOrm", back_populates="reviews")


