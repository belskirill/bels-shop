from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class ShopsOrm(Base):
    __tablename__ = 'shops'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    description: Mapped[str] = mapped_column(String)
    link_photo: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String, unique=True)
    status_open: Mapped[bool] = mapped_column(Boolean, default=False)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="shop")
    goods: Mapped[list["GoodsOrm"]] = relationship("GoodsOrm", back_populates="shop")
