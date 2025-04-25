from fastapi import APIRouter, Response, Request, Depends

from src.api.dependencies import DBDep, UserValidRefresh, UserIdDep, UserExpiredAccess, access_token_check
from src.exceptions import UserAlreadyExistsException, UserAlreadyExistsHTTPException, FailRegisterException, \
    FailRegisterHTTPException, UserNotFondHTTPException, UserNotFondException, FailedPasswordHTTPException, \
    FailedPasswordException, IncorrectPasswordHTTPException, IncorrectPasswordException
from src.schemas.users import UserRequestDTO, UserLoginDTO
from src.service.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register_user(data: UserRequestDTO, db: DBDep):
    try:
        await AuthService(db).register_user(data)
        return {"status": "OK"}
    except UserAlreadyExistsException:
        raise UserAlreadyExistsHTTPException
    except FailRegisterException:
        raise FailRegisterHTTPException


@router.post("/login")
async def login_user(data: UserLoginDTO, db: DBDep, response: Response):
    try:
        access_token = await AuthService(db).login_user(data)
        refresh_token = await AuthService(db).refresh_token(data)
        response.set_cookie("refresh_token", refresh_token)
        response.set_cookie("access_token", access_token)
        return {"access_token": access_token}
    except IncorrectPasswordException:
        raise IncorrectPasswordHTTPException
    except FailedPasswordException:
        raise FailedPasswordHTTPException
    except UserNotFondException:
        raise UserNotFondHTTPException


@router.post("/refresh")
async def refresh_access_token(
    request: Request, response: Response, db: DBDep, user: UserValidRefresh,
    check_access_token: bool = Depends(access_token_check)
):
    new_access_token = AuthService(db).create_access_token(
        {"user_id": user.id, "email": user.email, "shop_id": user.shop_id,
         "subscription_id": user.subscription_id, "number_phone": user.number_phone}
    )
    response.set_cookie("access_token", new_access_token)

    return {"access_token": new_access_token}
