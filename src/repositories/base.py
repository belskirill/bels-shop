from typing import Sequence

from dns.e164 import query
from pydantic import BaseModel

from src.database import Base
from src.repositories.mappers.base import DataMapper
from sqlalchemy import insert, select, update


class BaseRepository:
    model: type[Base]
    mapper: type[DataMapper]

    def __init__(self, session):
        self.session = session


    async def add_bulk(self, data: BaseModel):
        query = (
            insert(self.model)
            .values(data.model_dump()).returning(self.model)
        )

        res = await self.session.execute(query)
        model = res.scalars().one()
        return self.mapper.map_to_domain(model)

    async def add_big_bulk(self, data: Sequence[BaseModel]):
        query = (
            insert(self.model)
            .values(
                [item.model_dump() for item in data]
            )
        )

        await self.session.execute(query)


    async def get_one(self, **kwargs):
        query= (
            select(self.model)
            .filter_by(**kwargs)
        )

        res = await self.session.execute(query)
        model = res.scalars().one()
        return self.mapper.map_to_domain(model)


    async def get_all_data(self, **kwargs):
        query = (
            select(self.model).filter_by(**kwargs)
        )

        res = await self.session.execute(query)
        return [
            self.mapper.map_to_domain(model) for model in res.scalars().all()
        ]