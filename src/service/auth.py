from passlib.context import CryptContext

from src.exceptions import UserAlreadyExists, UserAlreadyExistsException, FailRegisterException
from src.schemas.users import UserRequestDTO, UserAdd
from src.service.base import BaseService


class AuthService(BaseService):
    pwd_context = CryptContext(
        schemes=["argon2", "bcrypt"], deprecated="auto", bcrypt__ident="2b"
    )


    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)


    async def register_user(self, data: UserRequestDTO):
        try:
            hashed_password = AuthService().hash_password(data.password)
            _data = UserAdd(
                first_name = data.first_name,
                last_name = data.last_name,
                email = data.email,
                password = hashed_password,
            )
            try:
                await self.db.users.add_user(_data)
                await self.db.commit()
            except UserAlreadyExists:
                raise UserAlreadyExistsException
        except Exception:
            raise FailRegisterException