import sys
from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from celery.backends.redis import RedisBackend
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.init import redis_manager



from src.api.auth import router as router_auth
from src.api.users import router as router_users
from src.api.shops import router as router_shops
from src.api.admin import router as router_admins


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_manager.connect()

    FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
    yield
    await redis_manager.close()


app = FastAPI(title='BELS-SHOP Docs')

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_shops)
app.include_router(router_admins)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)