from pydantic import BaseModel

from src.exceptions import ShopNotFoundEception, DubliateShopException, UserNofFoundException
from src.schemas.shop import ShopUpdateDTO
from src.service.base import BaseService
from src.time import download_image_user


class ShopsService(BaseService):

    async def get_info_shops(self, user):
        try:
            return await self.db.shops.get_all(user_id=user)
        except ShopNotFoundEception:
            raise ShopNotFoundEception

    async def create_shop(self, data: BaseModel, user_id):
        try:
            _data = ShopUpdateDTO(**data.model_dump(), user_id=user_id)
            res = await self.db.shops.add_data(_data)
            await self.db.commit()
            return res
        except DubliateShopException:
            raise DubliateShopException

    async def download_image(self, file, user):
        try:
            link = await download_image_user(file)
            await self.db.shops.edit_link_shop(user, link_photo=link)
            await self.db.commit()
            return link
        except RuntimeError:
            raise RuntimeError
        except UserNofFoundException:
            raise UserNofFoundException

    async def change_status(self, status, user):
        try:
            shop = await self.db.shops.change_status_db(status, user)
            await self.db.commit()
            if shop.status_open == True:
                return "Магазин открыт"
            if shop.status_open == False:
                return "Магазин закрыт"
        except UserNofFoundException:
            raise ShopNotFoundEception

    async def delete_shop(self, shop_id):
        try:
            await self.db.shops.delete_shops(shop_id)
            await self.db.commit()
        except ShopNotFoundEception:
            raise ShopNotFoundEception

    async def patch_edit_shop(self, user, data: BaseModel):
        try:
            return await self.db.shops.edit_shop(user, data)
        except UserNofFoundException:
            raise ShopNotFoundEception

    async def get_id_shop(self, shop_id):
        try:
            return await self.db.shops.get_all(id=shop_id)
        except ShopNotFoundEception:
            raise ShopNotFoundEception
