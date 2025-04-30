from sqlalchemy import insert, select, update, delete

from src.models import ShopsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ShopsDataMapper
from src.schemas.shop import ShopBaseDTO


class ShopsRepository(BaseRepository):
    model = ShopsOrm
    mapper = ShopsDataMapper



    async def get_all(self, **kwarg):
        query = (
            select(self.model)
            .filter_by(**kwarg)
        )

        results = await self.session.execute(query)
        model = results.scalars().one_or_none()
        if model is None:
            return None
        return self.mapper.map_to_domain(model)


    async def add_data(self, data):
        query = (
            insert(self.model)
            .values(**data.model_dump()).returning(self.model)
        )
        results = await self.session.execute(query)
        model = results.scalars().one()
        return self.mapper.map_to_domain(model)


    async def edit_link_shop(self, user, **filter_by) -> None:
        stmt_edit_hotel = (
            update(self.model)
            .filter_by(user_id=user)
            .values(**filter_by)
        )
        await self.session.execute(stmt_edit_hotel)


    async def get_all_shop_except(self):
        query = (
            select(self.model)
            .filter_by(confirmed=False)
        )

        results = await self.session.execute(query)
        model = results.scalars().one_or_none()
        if model is None:
            return None
        return self.mapper.map_to_domain(model)


    async def confirm_shop_db(self, shop_id):
        query = (
            update(self.model)
            .filter_by(id=shop_id)
            .values(confirmed=True)
        )
        await self.session.execute(query)

    async def change_status_db(self, status, user):
        query = (
            update(self.model)
            .filter_by(user_id=user)
            .values(status_open=status).returning(self.model)
        )

        results = await self.session.execute(query)
        model = results.scalars().one_or_none()
        return self.mapper.map_to_domain(model)


    async def delete_shops(self, shop_id):
        query = (
            delete(self.model)
            .filter_by(id=shop_id)
        )
        await self.session.execute(query)


    async def edit_shop(self, user, data):
        query = (
            update(self.model)
            .filter_by(user_id=user)
            .values(**data.model_dump(exclude_unset=True)).returning(self.model)
        )
        results = await self.session.execute(query)
        model = results.scalars().one_or_none()
        return self.mapper.map_to_domain(model)