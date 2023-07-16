from datetime import date

from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Rate


# class Rate_Pydantic(BaseModel):
#     cargo_type: str = Field(max_length=30)
#     actual_rate: float = Field(ge=0)
#     date: date


class DeclaredCost(BaseModel):
    cargo_type: str = Field(max_length=30)
    declared_cost: float = Field(ge=0)
    date: date


Rate_Pydantic = pydantic_model_creator(Rate, name="Rate_Pydantic")
RateIn_Pydantic = pydantic_model_creator(Rate, name="RateIn_Pydantic", exclude_readonly=True)
