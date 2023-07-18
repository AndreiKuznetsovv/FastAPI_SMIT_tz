from datetime import date
from typing import List

from pydantic import BaseModel


class RateInfo(BaseModel):
    cargo_type: str
    actual_rate: float


class RatesList(BaseModel):
    date: date
    rates_list: List[RateInfo]
