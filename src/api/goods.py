from fastapi import APIRouter


router = APIRouter(prefix="/goods", tags=["goods"])


@router.get("/my/goods")
async def get_my_goods():
    ...