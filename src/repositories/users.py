from sqlalchemy import insert, select, update

import logging

from asyncpg.exceptions import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from src.exceptions import UserAlreadyExists
from src.models.subscriptions import SubscriptionsOrm
from src.models.users import UsersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import UserDataMapper
from src.schemas.users import UserBase
from src.schemas.users_auth import UserEditDTO


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


    async def update_password(self, user_id, new_password):
        query = (
            update(self.model)
            .filter_by(id=user_id)
            .values(password=new_password)
        )

        await self.session.execute(query)


    async def user_edit_info(self, user_id, data):
        query = (
            update(self.model)
            .filter_by(id=user_id)
            .values(data.model_dump(exclude_unset=True))
        ).returning(self.model)
        results = await self.session.execute(query)
        model = results.scalars().one()
        return UserEditDTO.model_validate(model)

    async def get_user_base_info_model(self, user_id):
        query = (
            select(self.model)
            .options(joinedload(self.model.shop))
            .options(joinedload(self.model.subscription).joinedload(SubscriptionsOrm.tarif))
            .filter_by(id=user_id)
                 )
        results = await self.session.execute(query)
        model = results.scalars().one()
        return UserBase.model_validate(model, from_attributes=True)


    async def edit_link(self, user, **filter_by) -> None:
        stmt_edit_hotel = (
            update(self.model)
            .filter_by(id=user)
            .values(**filter_by)
        )
        await self.session.execute(stmt_edit_hotel)





