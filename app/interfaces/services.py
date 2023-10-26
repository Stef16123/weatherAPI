from abc import ABC, abstractmethod
from typing import Union
from core.models import Weather


class WeatherServiceInterface(ABC):
    repository = None
    
    @abstractmethod
    async def get_current_temperature(self) -> Union[int, float, None]:
        pass

    @abstractmethod
    async def get_last_hour_temperature(self) -> Union[int, float, None]:
        pass

    @abstractmethod
    async def get_historical_data(self) -> dict:
        pass

    @abstractmethod
    async def get_historical_data_max(self, data: list[Weather]) -> int:
        pass

    @abstractmethod
    async def get_historical_data_min(self, data: list[Weather]) -> int:
        pass
