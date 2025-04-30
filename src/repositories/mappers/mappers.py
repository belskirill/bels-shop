from src.models import ShopsOrm
from src.models.users import UsersOrm, PasswordChangeTokenOrm
from src.repositories.mappers.base import DataMapper
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