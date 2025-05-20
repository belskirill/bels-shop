from pydantic import BaseModel

from src.service.base import BaseService


class GoodsService(BaseService):


    async def create_goods_in_shops(self, data: BaseModel):
        res = await self.db.goods.add_bulk(data)
        await self.db.commit()
        return res


    async def get_id_good(self, good_id: int):
        res = await self.db.goods.get_one(id=good_id)
        await self.db.commit()
        return res


    async def get_all_goods_in_shop(self, user):
        shop = await self.db.shops.get_one(user_id=user)

        return await self.db.goods.get_all_data(shop_id=shop.id)