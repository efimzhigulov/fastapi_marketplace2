#!/bin/bash

alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000

python consumer.py new_order order_processing notification > logs_from_rabbit.log

