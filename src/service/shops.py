from pydantic import BaseModel

from src.schemas.shop import ShopUpdateDTO
from src.service.base import BaseService
from src.time import download_image_user


class ShopsService(BaseService):

    async def get_info_shops(self, user):
        return await self.db.shops.get_all(user_id=user)



    async def create_shop(self, data: BaseModel, user_id):
        _data = ShopUpdateDTO(**data.model_dump(), user_id=user_id)
        res = await self.db.shops.add_data(_data)
        await self.db.commit()
        return res


    async def download_image(self, file, user):
        link = await download_image_user(file)
        await self.db.shops.edit_link_shop(user, link_photo=link)
        await self.db.commit()
        return link


    async def change_status(self, status, user):
        shop = await self.db.shops.change_status_db(status, user)
        await self.db.commit()
        if shop.status_open == True:
            return "Магазин открыт"
        if shop.status_open == False:
            return "Магазин закрыт"

    async def delete_shop(self, shop_id):
        await self.db.shops.delete_shops(shop_id)
        await self.db.commit()


    async def patch_edit_shop(self, user, data: BaseModel):
        return await self.db.shops.edit_shop(user, data)

    async def get_id_shop(self, shop_id):
        return await self.db.shops.get_all(id=shop_id)

