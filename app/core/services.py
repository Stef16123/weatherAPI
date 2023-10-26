from core.config import API_KEY
from domain.api import get_current_conditions
from interfaces.services import WeatherServiceInterface
from repositories.weather import WeatherRepository
from core.models import Weather
from typing import Union


class WeatherService(WeatherServiceInterface):
    repository: WeatherRepository

    def __init__(self, db) -> None:
        super().__init__()
        self.db = db
        self.repository = WeatherRepository(db)

    async def get_current_temperature(self) -> Union[int, float, None]:
        response = await get_current_conditions(API_KEY)
        weather: Weather = await Weather.serialize_external_data(response[0])
        return weather.temperature
    
    async def get_last_hour_temperature(self) -> Union[int, float, None]:
        weather: Union[Weather, None] = await self.repository.get_last_hour()
        return weather.temperature if weather else None

    async def get_historical_data(self) -> list[Weather]:
        return await self.repository.get_historical()

    async def get_historical_data_max(self) -> Weather:
        data: list[Weather] = await self.get_historical_data()
        max: Weather = data[0]
        for historical in data:
            if max.temperature < historical.temperature:
                max = historical
        return max

    async def get_historical_data_min(self) -> Weather:
        data: list[Weather] = await self.get_historical_data()
        min: Weather = data[0]
        for historical in data:
            if min.temperature > historical.temperature:
                min = historical
        return min


