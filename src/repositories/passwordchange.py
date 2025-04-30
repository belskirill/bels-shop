from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete

from src.models.users import PasswordChangeTokenOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import PasswordChangeTokenOrmDataMapper


class PasswordChangeRepository(BaseRepository):
    model = PasswordChangeTokenOrm
    mapper = PasswordChangeTokenOrmDataMapper





    async def add_data(self, data: BaseModel):
        query = (
            insert(self.model)
            .values(data.model_dump())
        )

        await self.session.execute(query)


    async def get_data(self, user_id):
        query = (
            select(self.model)
            .filter_by(user_id=user_id, is_used=False)
        )
        results = await self.session.execute(query)
        model = results.scalars().one()
        return self.mapper.map_to_domain(model)


    async def edit_data(self, id):
        query = (
            update(self.model)
            .filter_by(id=id)
            .values(is_used=True)
        )
        await self.session.execute(query)

    async def delete_not_confirm(self):
        query = (
            delete(self.model)
            .filter(self.model.expires_at < datetime.utcnow() and self.model.is_used != True)
        )

        await self.session.execute(query)







    async def delete_not_confirm_user(self, user_id):
        query = (
            delete(self.model)
            .filter_by(user_id=user_id, is_used=False)
        )

        await self.session.execute(query)

