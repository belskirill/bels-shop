from src.service.base import BaseService


class ReviewsService(BaseService):

    async def get_reviews(self, goods_id):
        res = await self.db.reviews.get_reviews_with_user(goods_id)
        await self.db.commit()
        return res

    # todo: сделать в каждлм сервисе метод который будет проверять есть ли такой ид у
    #  них в базе или нет для проверок в каждом сервисе, например здесь для проверки
    #  есть ли такой товар по ид или нет что бы сразу выдавать ошибку
