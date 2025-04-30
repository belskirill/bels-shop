from fastapi import APIRouter, Query, UploadFile

from src.api.dependencies import UserIdDep, DBDep
from src.schemas.shop import ShopAddDTO, ShopPatchDTO
from src.service.shops import ShopsService

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("/my")
async def get_my_shops(user: UserIdDep, db: DBDep):
    return await ShopsService(db).get_info_shops(user)


@router.get("/shop_id")
async def get_shop(
    db: DBDep,
    user: UserIdDep,
    shop_id: int,
):
    return await ShopsService(db).get_id_shop(shop_id)


@router.post("/create")
async def create_shop(user: UserIdDep, db: DBDep, data: ShopAddDTO):
    return await ShopsService(db).create_shop(data, user_id=user)

@router.post("/image")
async def image_shop(
    user: UserIdDep,
    db: DBDep,
    file: UploadFile,
):
    response = await ShopsService(db).download_image(user=user, file=file)
    return {"status": "OK", "data": response}


@router.post("/status")
async def status_shop(
    user: UserIdDep,
    db: DBDep,
    status: bool = Query(description="status_shop"),
):
    response = await ShopsService(db).change_status(status=status, user=user)
    return {"status": "OK", "data": response}



@router.patch("/update")
async def update_shop(
    user: UserIdDep,
    db: DBDep,
    data: ShopPatchDTO
):
    return await ShopsService(db).patch_edit_shop(user, data)

@router.delete("")
async def delete_shop(
    user: UserIdDep,
    db: DBDep,
    shop_id: int = Query(description="shop_id"),
):
    await ShopsService(db).delete_shop(shop_id=shop_id)
    return {"status": "OK"}



