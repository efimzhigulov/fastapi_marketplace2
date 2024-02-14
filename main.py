from fastapi import FastAPI
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


app = FastAPI(
    title="Marketplace")


@app.get('/')
def hello():
    return ('hello')