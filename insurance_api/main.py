from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise
from rates import router


app = FastAPI(title="Insurance Calculation App")
app.include_router(router.rate_router)

register_tortoise(
    app,
    db_url="postgres://dron_test:2805@localhost/smit_test",
    modules={"models": ["rates.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)