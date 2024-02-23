from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()


orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("status", String, nullable=False),
    Column("delivery_address", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("users_id", Integer, ForeignKey("users.id")),
    Column("products_id", Integer, ForeignKey("products.id")),


)

status = Table(
    "status",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("status_id", Integer, ForeignKey("status.id")),
    Column("favorite_product_id", Integer, ForeignKey("products.id")),
)

shops = Table(
    "shops",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("Description", String,nullable=False),
    Column("email", String, nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("weight", Integer, nullable=False),
    Column("colour", Integer, nullable=False),
    Column("Description", String,nullable=False),
    Column("image_url", String),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("shop_id", Integer, ForeignKey("shops.id")),
    Column("category_id", Integer, ForeignKey("category.id")),
)

category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("Description", String,nullable=False),
    Column("number_of_products", Integer, nullable=False)
)

reviews_shops = Table(
    "reviews_shops",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("users_id", Integer, ForeignKey('users.id')),
    Column("shop_id", Integer, ForeignKey('shops.id')),
    Column("mark", Integer,nullable=False),
    Column("description", String),
)

reviews_products = Table(
    "reviews_products",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("users_id", Integer, ForeignKey('users.id')),
    Column("products_id", Integer, ForeignKey('products.id')),
    Column("mark", Integer,nullable=False),
    Column("description", String),
)
