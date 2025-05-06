from fastapi import APIRouter, UploadFile

from fastapi_cache.decorator import cache

from src.api.dependencies import UserIdDep, DBDep
from src.exceptions import FailedPasswordException, FailedPasswordHTTPException, PasswordChangeNotFoundException, \
    UserNofFoundException, UserNofFoundHTTPException, RuntimeErrorHTTPException, RuntimeErrorException, \
    PasswordChangeNotFoundHTTPException
from src.schemas.users import UsersRequest
from src.schemas.users_auth import UserInfoPatch
from src.service.users import UsersService

router = APIRouter(tags=["users"], prefix="/users")



@router.get("/me")
async def get_info(user: UserIdDep, db: DBDep):
    try:
        return await UsersService(db).get_user_base_info(user)
    except UserNofFoundException:
        raise UserNofFoundHTTPException

@router.patch("/edit")
async def edit_user_info(data: UserInfoPatch, db: DBDep, user: UserIdDep):
    try:
        response = await UsersService(db).edit_base_info(user, data)
        return {"data": response}
    except UserNofFoundException:
        raise UserNofFoundHTTPException


@router.post("/image/download")
async def edit_photo_user(db: DBDep, user: UserIdDep, file: UploadFile):
    try:
        response = await UsersService(db).edit_photo(user=user, file=file)
        return {
            "status": "OK",
            "link": response
        }
    except UserNofFoundException:
        raise UserNofFoundHTTPException
    except RuntimeErrorException:
        raise RuntimeErrorHTTPException


@router.post("/request-password-change")
async def request_password_change(data: UsersRequest, user: UserIdDep, db: DBDep):
    try:
        await UsersService(db).request_password_change(user=user, data=data)
        return {"status": "OK"}
    except FailedPasswordException:
        raise FailedPasswordHTTPException


@router.post("/change_confirmed_password")
async def change_confirmed_password(user: UserIdDep, db: DBDep):
    try:
        await UsersService(db).change_confirmed_password(user)
    except PasswordChangeNotFoundException:
        raise PasswordChangeNotFoundHTTPException