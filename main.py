from typing import AsyncGenerator, Annotated

import pytest
from fastapi import FastAPI, Depends
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import crud

from database import init_db, get_session
from models import users
#from database import database
from fastapi.testclient import TestClient

app = FastAPI(
    title="Marketplace")


@app.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


@app.get("/get_users")
async def get_users(session: AsyncSession = Depends(get_session)):
        query = select(users)
        result = await session.execute(query)
        return result.all()

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


async def test_get_users(ac: AsyncClient):
    response = await ac.get("/get_users", params={
        "username": "vasyan",
    })

    assert response.status_code == 200


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(get_session)]):
    return {"message": "Hello Items!", "params": commons}


