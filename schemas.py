from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    email: str
    username: str
    password: str
    registered_at: datetime

class OrderCreate(BaseModel):
    id: int
    status: str
    delivery_address: str
    registered_at: datetime


