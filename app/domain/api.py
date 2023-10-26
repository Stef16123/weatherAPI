import aiohttp
from domain.constants import MOSCOW_CODE 
from domain.url_builder import build_url_search_by_city, build_url_current_condition, build_url_current_condition_historical


async def get_search_by_city(city, API_KEY):
    url = await build_url_search_by_city()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'q': city, 'apikey': API_KEY}) as response:
            return await response.json()


async def get_current_conditions(API_KEY, location_key: int = MOSCOW_CODE):
    url = await build_url_current_condition(location_key)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'apikey': API_KEY}) as response:
            return await response.json()


async def get_current_conditions_historical(location_key, API_KEY):
    url = await build_url_current_condition_historical(location_key)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'apikey': API_KEY}) as response:
            return await response.json()

