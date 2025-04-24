from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.exceptions import UserAlreadyExistsException, UserAlreadyExistsHTTPException, FailRegisterException, \
    FailRegisterHTTPException
from src.schemas.users import UserRequestDTO
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
