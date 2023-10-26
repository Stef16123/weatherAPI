from domain.constants import SEARCH_BY_CITY, CURRENT_CONDITIONS


async def build_url_search_by_city():
    return SEARCH_BY_CITY

async def build_url_current_condition(location_key):
    return f'{CURRENT_CONDITIONS}/{location_key}'

async def build_url_current_condition_historical(location_key):
    return f'{CURRENT_CONDITIONS}/{location_key}/historical/24'
