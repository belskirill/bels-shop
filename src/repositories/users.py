from sqlalchemy import insert

from asyncpg.exceptions import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from src.exceptions import UserAlreadyExists
from src.models.users import UsersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import UserDataMapper


class UsersRepository(BaseRepository):
    model = UsersOrm
    mapper = UserDataMapper

    def __init__(self, session):
        self.session = session

    async def add_user(self, data):
        query = (
            insert(self.model)
            .values(**data.model_dump())
        )

        try:
            await self.session.execute(query)
        except IntegrityError as ex:
            if isinstance(ex.orig.__cause__, UniqueViolationError):
                raise UserAlreadyExists
