from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger, ForeignKey

from src.database import Base


class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    shop_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("shops.id"), nullable=True)
    link_photo: Mapped[str] = mapped_column(String)
    about_me: Mapped[str] = mapped_column(String)
    subscription_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriptions.id"), nullable=True)