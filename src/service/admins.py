from src.service.base import BaseService
from src.tasks.tasks import info_email_confirm_shop


class AdminsService(BaseService):
    async def get_except_shops(self):
        return await self.db.shops.get_all_shop_except()


    async def confirm_shop(self, shop_id, email):
        await self.db.shops.confirm_shop_db(shop_id)
        await self.db.commit()
        info_email_confirm_shop.delay(email)