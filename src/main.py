import sys
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from celery.backends.redis import RedisBackend
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

sys.path.append(str(Path(__file__).parent.parent))

from src.init import redis_manager



from src.api.auth import router as router_auth
from src.api.users import router as router_users
from src.api.shops import router as router_shops
from src.api.reviews import router as router_reviews
from src.api.goods import router as router_goods
from src.api.admin import router as router_admins



from fastapi_cache import FastAPICache  # noqa: E402
from fastapi_cache.backends.redis import RedisBackend  # noqa: E402


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_manager.connect()

    FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
    yield
    await redis_manager.close()


app = FastAPI(title='BELS-SHOP Docs', lifespan=lifespan)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_shops)
app.include_router(router_reviews)
app.include_router(router_goods)
app.include_router(router_admins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)