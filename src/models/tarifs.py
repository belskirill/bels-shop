

from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy.testing.schema import mapped_column

from src.database import Base


class TarifsOrm(Base):
    __tablename__ = 'tarifs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)