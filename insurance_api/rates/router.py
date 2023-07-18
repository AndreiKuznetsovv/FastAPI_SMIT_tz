from typing import Annotated

from fastapi import APIRouter, Header

from .schemas import RatesList
from .services import (
    get_rate,
    calculate_cost,
    upload_rates
)

rate_router = APIRouter()


@rate_router.get('/rate')
async def get_cost(cargo_type: Annotated[str, Header()],
                   declared_cost: Annotated[float, Header()], date_uploaded: Annotated[str, Header()]):
    rate = await get_rate(cargo_type=cargo_type, date_uploaded=date_uploaded)
    cost = await calculate_cost(declared_cost=declared_cost, rate=rate)
    return {'calculated_cost': cost}


@rate_router.post('/rate')
async def post_rate(list_of_rates: RatesList):
    uploaded_rates = await upload_rates(list_of_rates=list_of_rates)
    return {f'{uploaded_rates[0].date.date}':
                [{'cargo_type': rate.cargo_type.cargo_type, 'rate': rate.actual_rate} for rate in uploaded_rates]}
