from typing import Annotated

from fastapi import APIRouter, Header

from .schemas import (
    Rate_Pydantic,
    RateIn_Pydantic,
)
from .services import (
    get_rate,
    calculate_cost,
    upload_rate
)

rate_router = APIRouter()


@rate_router.get('/rate')
async def get_cost(cargo_type: Annotated[str, Header()],
                   declared_cost: Annotated[float, Header()], date_posted: Annotated[str, Header()]):
    rate = await get_rate(cargo_type=cargo_type, date_posted=date_posted)
    cost = await calculate_cost(declared_cost=declared_cost, rate=rate)
    return {'calculated_cost': cost}


@rate_router.post('/rate')
async def post_rate(rate: RateIn_Pydantic):
    new_rate = await upload_rate(rate=rate)
    return await Rate_Pydantic.from_tortoise_orm(new_rate)
