from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
import logging
from fastapi import HTTPException
import jwt

from src.exceptions import UserAlreadyExists, UserAlreadyExistsException, FailRegisterException, \
    IncorrectPasswordException, FailedPasswordException, UserNotFondException
from src.schemas.users import UserRequestDTO, UserAdd
from src.service.base import BaseService
from src.config import settigns


class AuthService(BaseService):
    pwd_context = CryptContext(
        schemes=["argon2", "bcrypt"], deprecated="auto", bcrypt__ident="2b"
    )

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settigns.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settigns.JWT_SECRET_KEY, algorithm=settigns.JWT_ALGORITHM
        )
        return encoded_jwt

    def create_refresh_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=settigns.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({
            "exp": expire,
            "type": "refresh"  # отличаем тип токена
        })
        return jwt.encode(to_encode, settigns.JWT_SECRET_KEY, algorithm=settigns.JWT_ALGORITHM)


    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, token: str) -> dict:
        try:
            return jwt.decode(
                token,
                settigns.JWT_SECRET_KEY,
                algorithms=[settigns.JWT_ALGORITHM],
            )
        except jwt.exceptions.DecodeError:
            raise HTTPException(status_code=401, detail="Неверный токен!")

    async def register_user(self, data: UserRequestDTO):
        try:
            hashed_password = AuthService().hash_password(data.password)
            _data = UserAdd(
                first_name=data.first_name,
                last_name=data.last_name,
                email=data.email,
                password=hashed_password,
            )
            try:
                await self.db.users.add_user(_data)
                await self.db.commit()
            except UserAlreadyExists:
                raise UserAlreadyExistsException
        except Exception:
            raise FailRegisterException

    async def login_user(self, data):
        if data.password:
            logging.warning(data.email)
            user = await self.db.users.get_user_with_hashed_password(
                email=data.email
            )
            logging.warning(user)
            if not user:
                raise UserNotFondException
            if not AuthService().verify_password(
                data.password, user.password
            ):
                raise FailedPasswordException
            access_token = AuthService().create_access_token(
                {"user_id": user.id, "email": user.email, "shop_id": user.shop_id,
                 "subscription_id": user.subscription_id, "number_phone": user.number_phone}
            )
            return access_token
        else:
            raise IncorrectPasswordException

    async def refresh_token(self, data):
        user = await self.db.users.get_user_with_hashed_password(
            email=data.email
        )
        refresh_token = AuthService().create_refresh_token(
            {"user_id": user.id, "email": user.email, "shop_id": user.shop_id,
             "subscription_id": user.subscription_id, "number_phone": user.number_phone}
        )
        return refresh_token
