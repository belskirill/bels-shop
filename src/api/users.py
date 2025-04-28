from fastapi import APIRouter

from src.api.dependencies import UserIdDep, DBDep
from src.schemas.users import UsersRequest
from src.service.users import UsersService

router = APIRouter(tags=["users"], prefix="/users")


@router.post("/request-password-change")
async def request_password_change(data: UsersRequest, user: UserIdDep, db: DBDep):
    await UsersService(db).request_password_change(user=user, data=data)


@router.post("/change_confirmed_password")
async def change_confirmed_password():
    ...
