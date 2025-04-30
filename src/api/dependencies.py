from typing import Annotated
import jwt
from src import time

from fastapi import Depends, Request, HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError


from src.database import async_session_maker
from src.service.auth import AuthService
from src.utils.db_manager import DBManager


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]




def check_login(request: Request):
    token = request.cookies.get("access_token", None)
    token_refresh = request.cookies.get("refresh_token", None)
    if token or token_refresh:
        raise HTTPException(
            status_code=409,
            detail="Вы уже авторизованы!",
        )


ChechLogin = Annotated[None, Depends(check_login)]


def check_no_login(request: Request):
    token = request.cookies.get("access_token", None)
    token_refresh = request.cookies.get("refresh_token", None)
    if not token or not token_refresh:
        raise HTTPException(
            status_code=409,
            detail="Вы не авторизованы!",
        )


CheckNoLogin = Annotated[None, Depends(check_no_login)]

async def refresh_check(request: Request, db: DBDep):
    try:
        # Получаем refresh_token из куки
        refresh_token = request.cookies.get("refresh_token")

        if not refresh_token:
            raise HTTPException(status_code=401, detail="Refresh token not found")

        # Декодируем refresh_token и проверяем его валидность
        decoded_refresh_token = AuthService(db).encode_token(refresh_token)


        # Проверяем тип токена и извлекаем информацию о пользователе
        if decoded_refresh_token.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        user_id = decoded_refresh_token.get("user_id")
        user = await db.users.get_user(user_id)

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")


UserValidRefresh = Annotated[None, Depends(refresh_check)]



def get_token(request: Request) -> str:
    token = request.cookies.get("access_token", None)
    if not token:
        raise HTTPException(
            status_code=401, detail="Вы не предоставили токен доступа!"
        )
    return token


def current_user_id(token: str = Depends(get_token)) -> int:
    try:
        data = AuthService().encode_token(token)
        return data["user_id"]
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Срок действия токена истёк",
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Недействительный токен",
        )


UserIdDep = Annotated[int, Depends(current_user_id)]


def current_user_email(token: str = Depends(get_token)) -> int:
    try:
        data = AuthService().encode_token(token)
        return data["email"]
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Срок действия токена истёк",
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Недействительный токен",
        )

UserEDep = Annotated[str, Depends(current_user_email)]



async def access_token_check(request: Request):
    try:
        access_token = request.cookies.get("access_token")
        if not access_token:
            raise HTTPException(status_code=401, detail="access_token не найден")

        decoded_access_token = AuthService().encode_token(access_token)

        if decoded_access_token is None:
            return None

        if decoded_access_token.get("exp") > int(time.time()):
            raise HTTPException(status_code=409, detail="У вас активный токен!")

        return None

    except ExpiredSignatureError:
        return None
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Неверный access_token")


UserExpiredAccess = Annotated[None, Depends(access_token_check)]


