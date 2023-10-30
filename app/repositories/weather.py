from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
from core.models import Weather
from interfaces.repositories import WeatherRepositoryInterface
from typing import Union


class WeatherRepository(WeatherRepositoryInterface):
    db: AsyncIOMotorClient

    def __init__(self, db) -> None:
        super().__init__()
        self.db = db
    
    async def save(self, weather: Weather) -> None:
        await self.db.manager.weathers.insert_one(weather.model_dump())
    
    async def get_last_hour(self) -> Union[Weather, None]:
        query = {"datetime": {"$gte": datetime.now() - timedelta(hours=1)}}
        weather_data = await self.db.manager.weathers.find_one(query)
        if not weather_data:
            return None
        return Weather.model_validate(weather_data)

    async def get_historical(self) -> list[Weather]:
        query = {
            'datetime': {
                '$gt' : datetime.now().replace(minute=0, second=0) - timedelta(hours=24)
            }
        }
        return [Weather(**weather) for weather in await self.db.manager.weathers.find(query).to_list(24)]
    