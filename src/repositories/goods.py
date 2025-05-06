from src.models import GoodsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import GoodsDataMapper



class GoodsRepository(BaseRepository):
    model = GoodsOrm
    mapper = GoodsDataMapper

