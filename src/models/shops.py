from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class ShopsOrm(Base):
    __tablename__ = 'shops'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    link_photo: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String, unique=True)
    status_open: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="shop")