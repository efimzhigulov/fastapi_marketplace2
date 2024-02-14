from datetime import datetime

from sqlalchemy import MetaData, Column, ForeignKey, Integer, String, TIMESTAMP

from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    favorite_product_id = Column(Integer, ForeignKey("products.id"))
    status = Column(String, nullable=False)
class Shops(Base):
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    Description = Column(String,nullable=False)
    email = Column(String, nullable=False)

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    colour = Column(Integer, nullable=False)
    Description = Column(String,nullable=False)
    image_url = Column(String)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    shop_id = Column(Integer, ForeignKey("shops.id"))
    category_id = Column(Integer, ForeignKey("category.id"))

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    Description = Column(String,nullable=False)
    number_of_products = Column(Integer, nullable=False)


class Rewies_shops(Base):
    __tablename__ = "rewies_shops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))
    mark = Column(Integer,nullable=False)
    description = Column(String)

class Rewies_products(Base):
    __tablename__ = "rewies_products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    products_id = Column(Integer, ForeignKey('products.id'))
    mark = Column(Integer,nullable=False)
    description = Column(String)
