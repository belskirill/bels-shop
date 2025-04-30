from pathlib import Path

from httpx import AsyncClient
from httpx import ASGITransport

import pytest

from src.api.dependencies import get_db
from src.config import settigns
from src.database import async_session_maker_null_pool, engine_null_pool, Base
from src.main import app
from src.utils.db_manager import DBManager


current_dir = Path(__file__).parent

@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    assert settigns.MODE == "TEST"


@pytest.fixture(scope="function")
async def db():
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        yield db


async def get_db_null_pool():
    async with DBManager(session_factory=async_session_maker_null_pool) as db:
        yield db


app.dependency_overrides[get_db] = get_db_null_pool


@pytest.fixture(scope="session", autouse=True)
async def database_setup(check_test_mode):
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
async def ac():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture(scope="session", autouse=True)
async def async_client(ac, database_setup):
    await ac.post(
        "/auth/register",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "kirill666777@test.ru",
            "password": "string",
        },
    )


@pytest.fixture(scope="session")
async def authenticated_ac(async_client, ac):
    await ac.post(
        "/auth/login",
        json={
            "email": "kirill666777@test.ru",
            "password": "string",
        },
    )

    assert ac.cookies["access_token"]
    yield ac