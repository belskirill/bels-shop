from fastapi import APIRouter


router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("/goods/reviews")
async def get_reviews():
    ...