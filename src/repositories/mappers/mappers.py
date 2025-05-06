from src.models import ShopsOrm, GoodsOrm, UsersOrm, ReviewsOrm
from src.models.users import PasswordChangeTokenOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.goods import GoodsDTO
from src.schemas.reviews import ReviewsDTO
from src.schemas.shop import ShopBaseDTO
from src.schemas.users import UsersResponsePassword
from src.schemas.users_auth import UserDTO


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserDTO


class PasswordChangeTokenOrmDataMapper(DataMapper):
    db_model = PasswordChangeTokenOrm
    schema = UsersResponsePassword


class ShopsDataMapper(DataMapper):
    db_model = ShopsOrm
    schema = ShopBaseDTO


class GoodsDataMapper(DataMapper):
    db_model = GoodsOrm
    schema = GoodsDTO


class ReviewsDataMapper(DataMapper):
    db_model = ReviewsOrm
    schema = ReviewsDTO
