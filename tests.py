from typing import AsyncGenerator
from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

@pytest.mark.parametrize('url,params',[
    ("/get_users", {"username": "vasyan",}),
    ("/get_users", {"username": "petya888",}),
    ("/get_usrs", {"username": "petya888",})
])
async def test_get_users(url, params, ac: AsyncClient):
    response = await ac.get(url=url, params=params)

    assert response.status_code == 200

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}