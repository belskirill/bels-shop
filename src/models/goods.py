from sqlalchemy import String, Boolean, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class GoodsOrm(Base):
    __tablename__ = 'goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    link_photo: Mapped[str] = mapped_column(String, nullable=True)
    price_one: Mapped[int] = mapped_column(BigInteger, nullable=False)
    about: Mapped[str] = mapped_column(String, nullable=True)
    grade: Mapped[int] = mapped_column(BigInteger, nullable=True)
    shop_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('shops.id'), nullable=False)
    count: Mapped[int] = mapped_column(BigInteger, nullable=False)

    reviews: Mapped[list["ReviewsOrm"]] = relationship("ReviewsOrm", back_populates="goods")
    shop: Mapped["ShopsOrm"] = relationship("ShopsOrm", back_populates="goods")
