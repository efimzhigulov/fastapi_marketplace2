import logging
from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from emit_log_direct import rabbit
from models import users, orders
from schemas import OrderCreate

logging.basicConfig(
    level=logging.DEBUG,
    filename ="mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('starting app')


app = FastAPI(
    title="Marketplace")


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/get_users")
async def get_users(session: AsyncSession = Depends(get_session)):
        query = select(users)
        result = await session.execute(query)
        logging.info(result.all())
        return result.all()



@app.post("/add_order")
async def add_order(new_operation: OrderCreate, session: AsyncSession = Depends(get_session)):
    stmt = insert(orders).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    resp = str((new_operation).dict()['id'])
    resp2 = str((new_operation).dict()['status'])
    resp3 = str((new_operation).dict()['registered_at'])
    rabbit('new_order', resp)
    rabbit('order_processing',resp2)
    rabbit('notification', resp3)
    return new_operation



