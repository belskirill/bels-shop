from src.database import Base
from src.repositories.mappers.base import DataMapper
from sqlalchemy import insert, select, update


class BaseRepository:
    model: type[Base]
    mapper: type[DataMapper]

    def __init__(self, session):
        self.session = session

