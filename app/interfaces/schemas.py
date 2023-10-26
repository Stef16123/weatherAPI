from pydantic import BaseModel
from core.models import Weather


class WeatherList(BaseModel):
    list: list[Weather]
