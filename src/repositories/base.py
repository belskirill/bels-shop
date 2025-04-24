from src.database import Base
from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model: type[Base]
    mapper: type[DataMapper]