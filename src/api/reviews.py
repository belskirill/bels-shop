

from fastapi import APIRouter, WebSocket


from src.api.dependencies import DBDep, UserIdDep
from src.service.reviews import ReviewsService

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.get("/goods")
async def get_reviews(
    good_id: int,
    user: UserIdDep,
    db: DBDep,
):
    return await ReviewsService(db).get_reviews(good_id)


@router.post("/goods")
async def create_review():
    ...


@router.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    await websocket.send_text(data)