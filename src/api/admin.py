import logging

from src.service.shops import ShopsService

from fastapi import APIRouter, Query

from src.api.dependencies import UserIdDep, DBDep, UserEDep
from src.service.admins import AdminsService

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/shops_except")
async def get_shops_except(
    user: UserIdDep,
    db: DBDep
):
    return await AdminsService(db).get_except_shops()


@router.post("/accept_shops")
async def accept_shops(
    user: UserIdDep,
    email: UserEDep,
    db: DBDep,
    shop_id: int = Query(description="shop_id")
):
    logging.warning(email)
    await AdminsService(db).confirm_shop(shop_id, email)
    return {"status": "OK"}