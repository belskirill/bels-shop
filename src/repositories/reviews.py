from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.models import ReviewsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ReviewsDataMapper
from src.schemas.reviews import ReviewsGetDTO


class ReviewsRepository(BaseRepository):
    model = ReviewsOrm
    mapper = ReviewsDataMapper


    async def get_reviews_with_user(self, good_id):
        query = (
            select(self.model)
            .options(joinedload(self.model.user))
            .filter_by(goods_id=good_id)
        )

        results = await self.session.execute(query)
        model = results.scalars().all()
        return [
            ReviewsGetDTO.model_validate(m) for m in model
        ]