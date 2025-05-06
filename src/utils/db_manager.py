from sqlalchemy import delete

from src.repositories.goods import GoodsRepository
from src.repositories.passwordchange import PasswordChangeRepository
from src.repositories.reviews import ReviewsRepository
from src.repositories.shops import ShopsRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.password_change = PasswordChangeRepository(self.session)
        self.shops = ShopsRepository(self.session)
        self.goods = GoodsRepository(self.session)
        self.reviews = ReviewsRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()



