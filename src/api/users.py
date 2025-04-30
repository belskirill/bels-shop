from fastapi import APIRouter, UploadFile

from fastapi_cache.decorator import cache

from src.api.dependencies import UserIdDep, DBDep
from src.schemas.users import UsersRequest
from src.schemas.users_auth import UserInfoPatch
from src.service.users import UsersService

router = APIRouter(tags=["users"], prefix="/users")



@router.get("/me")
async def get_info(user: UserIdDep, db: DBDep):
    return await UsersService(db).get_user_base_info(user)

@router.patch("/edit")
async def edit_user_info(data: UserInfoPatch, db: DBDep, user: UserIdDep):
    response = await UsersService(db).edit_base_info(user, data)
    return {"data": response}


@router.post("/image/download")
async def edit_photo_user(db: DBDep, user: UserIdDep, file: UploadFile):
    response = await UsersService(db).edit_photo(user=user, file=file)
    return {
        "status": "OK",
        "link": response
    }



@router.post("/request-password-change")
async def request_password_change(data: UsersRequest, user: UserIdDep, db: DBDep):
    await UsersService(db).request_password_change(user=user, data=data)


@router.post("/change_confirmed_password")
async def change_confirmed_password(user: UserIdDep, db: DBDep):
    await UsersService(db).change_confirmed_password(user)
