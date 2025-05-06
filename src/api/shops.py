from fastapi import APIRouter, Query, UploadFile

from src.api.dependencies import UserIdDep, DBDep
from src.exceptions import ShopNotFoundHTTPException, ShopNotFoundEception, MyShopNotFoundHTTPException, \
    DubliateShopException, DubliateShopHTTPException, ErrorFormatImageHTTPException, UserNofFoundException, \
    UserNofFoundHTTPException, RuntimeErrorHTTPException
from src.schemas.shop import ShopAddDTO, ShopPatchDTO
from src.service.shops import ShopsService

router = APIRouter(prefix="/shops", tags=["shops"])


@router.get("/my")
async def get_my_shops(user: UserIdDep, db: DBDep):
    try:
        return await ShopsService(db).get_info_shops(user)
    except ShopNotFoundEception:
        raise MyShopNotFoundHTTPException


@router.get("/shop_id")
async def get_shop(
    db: DBDep,
    user: UserIdDep,
    shop_id: int,
):
    try:
        return await ShopsService(db).get_id_shop(shop_id)
    except ShopNotFoundEception:
        raise ShopNotFoundHTTPException


@router.post("/create")
async def create_shop(user: UserIdDep, db: DBDep, data: ShopAddDTO):
    try:
        return await ShopsService(db).create_shop(data, user_id=user)
    except DubliateShopException:
        raise DubliateShopHTTPException

@router.post("/image")
async def image_shop(
    user: UserIdDep,
    db: DBDep,
    file: UploadFile,
):
    if file not in ["image/png", "image/jpg", "images/jpeg"]:
        raise ErrorFormatImageHTTPException
    try:
        response = await ShopsService(db).download_image(user=user, file=file)
        return {"status": "OK", "data": response}
    except UserNofFoundException:
        raise UserNofFoundHTTPException
    except RuntimeError:
        raise RuntimeErrorHTTPException


@router.post("/status")
async def status_shop(
    user: UserIdDep,
    db: DBDep,
    status: bool = Query(description="status_shop"),
):
    try:
        response = await ShopsService(db).change_status(status=status, user=user)
        return {"status": "OK", "data": response}
    except UserNofFoundException:
        raise MyShopNotFoundHTTPException




@router.patch("/update")
async def update_shop(
    user: UserIdDep,
    db: DBDep,
    data: ShopPatchDTO
):
    try:
        return await ShopsService(db).patch_edit_shop(user, data)
    except ShopNotFoundEception:
        raise MyShopNotFoundHTTPException

@router.delete("")
async def delete_shop(
    user: UserIdDep,
    db: DBDep,
    shop_id: int = Query(description="shop_id"),
):
    try:
        await ShopsService(db).delete_shop(shop_id=shop_id)
        return {"status": "OK"}
    except ShopNotFoundEception:
        raise ShopNotFoundHTTPException



