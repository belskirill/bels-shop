from pydantic import BaseModel
from sqlalchemy import insert

from src.models.users import PasswordChangeTokenOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import PasswordChangeTokenOrmDataMapper


class PasswordChangeRepository(BaseRepository):
    model = PasswordChangeTokenOrm
    mapper = PasswordChangeTokenOrmDataMapper


    def __init__(self, session):
        self.session = session


    async def add_data(self, data: BaseModel):
        query = (
            insert(self.model)
            .values(data.model_dump())
        )

        await self.session.execute(query)

