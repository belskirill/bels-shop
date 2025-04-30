from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BigInteger, ForeignKey, Integer, DateTime, Boolean

from src.database import Base


class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    number_phone: Mapped[str] = mapped_column(String, nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String)
    link_photo: Mapped[str] = mapped_column(String, nullable=True)
    about_me: Mapped[str] = mapped_column(String, nullable=True)
    subscription_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("subscriptions.id"), nullable=True)

    shop: Mapped["ShopsOrm"] = relationship("ShopsOrm", back_populates="user", uselist=False)

    # 🔁 Many-to-one: пользователь → подписка
    subscription: Mapped["SubscriptionsOrm"] = relationship("SubscriptionsOrm", back_populates="users")

    password_change_tokens: Mapped[list["PasswordChangeTokenOrm"]] = relationship(
        "PasswordChangeTokenOrm", back_populates="user"
    )


class PasswordChangeTokenOrm(Base):
        __tablename__ = "password_change_tokens"

        id: Mapped[int] = mapped_column(primary_key=True)
        user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
        token: Mapped[str] = mapped_column(String, unique=True, nullable=False)
        new_password_hash: Mapped[str] = mapped_column(String, nullable=False)
        expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
        is_used: Mapped[bool] = mapped_column(Boolean, default=False)

        user: Mapped["UsersOrm"] = relationship("UsersOrm", back_populates="password_change_tokens")
