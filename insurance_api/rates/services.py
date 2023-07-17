from datetime import date
from typing import List

from .models import Rate, CargoType, DateUploaded
from .schemas import RatesList


async def get_rate(cargo_type: str, date_posted: str) -> Rate:
    rate = await Rate.filter(
        cargo_type=cargo_type, date=date_posted).first()
    return rate


async def calculate_cost(declared_cost: float, rate: Rate) -> float:
    calculated_cost = declared_cost * rate.actual_rate
    return calculated_cost


async def upload_cargo_type(cargo_type: str):
    return await CargoType.get_or_create(cargo_type=cargo_type)


async def upload_date(date: date):
    return await DateUploaded.get_or_create(date=date)


async def upload_rates(list_of_rates: RatesList) -> List[Rate]:
    uploaded_rates = []
    for rate in list_of_rates.rates_list:
        # create new instances for date and cargo_type (if they don't exist)
        cargo_type = await upload_cargo_type(cargo_type=rate.cargo_type)
        date = await upload_date(date=list_of_rates.date)
        # create new instance for rate
        new_rate = await Rate.create(actual_rate=rate.actual_rate,
                                     cargo_type=cargo_type[0], date=date[0])
        uploaded_rates.append(new_rate)
    return uploaded_rates
