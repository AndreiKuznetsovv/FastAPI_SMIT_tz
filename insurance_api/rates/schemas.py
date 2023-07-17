from datetime import date
from typing import List

from pydantic import BaseModel


class RateInfo(BaseModel):
    cargo_type: str
    actual_rate: float


class RatesList(BaseModel):
    date: date
    rates_list: List[RateInfo]

# Rate_Pydantic = pydantic_model_creator(Rate, name="Rate_Pydantic")
# RateIn_Pydantic = pydantic_model_creator(Rate, name="RateIn_Pydantic", exclude_readonly=True)
