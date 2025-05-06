from src.models import ReviewsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ReviewsDataMapper


class ReviewsRepository(BaseRepository):
    model = ReviewsOrm
    mapper = ReviewsDataMapper