from abc import ABC, abstractmethod
from datetime import datetime
from core.models import Weather

class WeatherRepositoryInterface(ABC):

    @abstractmethod
    async def save(self) -> None:
        pass

    @abstractmethod
    async def get_last_hour(self) -> Weather:
        pass

    @abstractmethod
    async def get_historical(self, datetime: datetime) -> list[Weather]:
        pass
