from sqlalchemy import insert, select

import logging

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


    async def get_user_with_hashed_password(self, email):

            query = select(self.model).filter_by(email=email)
            results = await self.session.execute(query)
            model = results.scalars().one()
            return self.mapper.map_to_domain(model)


    async def get_user(self, user_id):
        query = select(self.model).filter_by(id=user_id)
        results = await self.session.execute(query)
        model = results.scalars().one()
        return self.mapper.map_to_domain(model)

