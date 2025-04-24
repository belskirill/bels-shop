from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database import Base


class ShopsOrm(Base):
    __tablename__ = 'shops'

    id: Mapped[int] = mapped_column(primary_key=True)
    link_photo: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String, unique=True)
    status_open: Mapped[bool] = mapped_column(Boolean, default=False)