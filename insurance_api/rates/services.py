from .models import Rate
from .schemas import RateIn_Pydantic


async def get_rate(cargo_type: str, date_posted: str) -> Rate:
    rate = await Rate.filter(
        cargo_type=cargo_type, date=date_posted).first()
    return rate


async def calculate_cost(declared_cost: float, rate: Rate) -> float:
    calculated_cost = declared_cost * rate.actual_rate
    return calculated_cost


async def upload_rate(rate: RateIn_Pydantic) -> Rate:
    # new_rate = await Rate.create(**rate.dict())
    new_rate = await Rate.create(actual_rate=rate.actual_rate, cargo_type=rate.cargo_type, date=rate.date)
    return new_rate
