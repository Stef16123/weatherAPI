import logging
from core.models import Weather
from domain.api import get_current_conditions
from repositories.weather import WeatherRepository
from core.database import MongoDatabase

class Task:
    db: MongoDatabase
    API_KEY: str

    def __init__(self, db: MongoDatabase, API_KEY: str):
        self.db = db
        self.API_KEY = API_KEY

    async def fetch_current_data(self) -> None:
        logging.info('fetch current data...')
        response = await get_current_conditions(self.API_KEY)
        try:
            await WeatherRepository(self.db).save(await Weather.deserialize_external_data(response[0]))
        except Exception as e:
            raise e