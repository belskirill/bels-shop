from src.exceptions import NoResultFoundException, ShopNotFoundEception
from src.service.base import BaseService
from src.tasks.tasks import info_email_confirm_shop


class AdminsService(BaseService):
    async def get_except_shops(self):
        try:
            return await self.db.shops.get_all_shop_except()
        except NoResultFoundException:
            raise NoResultFoundException



    async def confirm_shop(self, shop_id, email):
        try:
            await self.db.shops.confirm_shop_db(shop_id)
            await self.db.commit()
            info_email_confirm_shop.delay(email)
        except ShopNotFoundEception:
            raise ShopNotFoundEception
