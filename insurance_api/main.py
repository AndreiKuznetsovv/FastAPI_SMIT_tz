from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import Config
from rates import router

app = FastAPI(title="Insurance Calculation App")
app.include_router(router.rate_router)

register_tortoise(
    app,
    db_url=Config.TORTOISE_DATABASE_URI,
    modules={"models": ["rates.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
