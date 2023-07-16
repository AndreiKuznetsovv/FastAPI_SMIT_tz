from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Rate

Rate_Pydantic = pydantic_model_creator(Rate, name="Rate_Pydantic")
RateIn_Pydantic = pydantic_model_creator(Rate, name="RateIn_Pydantic", exclude_readonly=True)
