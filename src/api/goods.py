

from fastapi import APIRouter, Query

from src.api.dependencies import DBDep, UserIdDep
from src.schemas.goods import GoodsCreateDTO
from src.service.goods import GoodsService

router = APIRouter(prefix="/goods", tags=["goods"])



@router.get("/goods/id")
async def get_my_goods(
    db: DBDep,
    user: UserIdDep,
    good_id: int = Query(description="id good"),
):
    return await GoodsService(db).get_id_good(good_id)



@router.get("")
async def get_all_goods_in_shop(
    user: UserIdDep,
    db: DBDep,
):
    return await GoodsService(db).get_all_goods_in_shop(user)

@router.get("/all")
async def get_all_goods(

):
    ...



@router.post("")
async def create_goods(
    db: DBDep,
    user: UserIdDep,
    data: GoodsCreateDTO,
):
    return await GoodsService(db).create_goods_in_shops(data)