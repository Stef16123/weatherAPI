import json
from fastapi import APIRouter
from core.models import Weather
from interfaces.schemas import WeatherList
from core.services import WeatherService
from core.config import db
from bson import json_util


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)
    

@router.get('/test')
async def test():
    return await db.manager.list_collection_names()

@router.get("/last-hour")
async def get_last_hour():
    service = WeatherService(db)
    temperature = await service.get_last_hour_temperature()
    if not temperature:
        return {'message': 'weather temperature on the last hour is not found'}
    return {'message': f'weather temperature on the last hour is {temperature} C'}

@router.get("/current")
async def get_current():
    service = WeatherService(db)
    temperature = await service.get_current_temperature()
    if not temperature:
        return {'message': 'current weather temperature is not found'}
    return {'message': f'current weather temperature is {temperature} C'}

@router.get('/historical')
async def get_historical():
    service = WeatherService(db)
    hist: list[Weather] =  await service.get_historical_data()
    return WeatherList(list=hist)

@router.get('/historical/max')
async def get_historical_max():
    service = WeatherService(db)
    weather = await service.get_historical_data_max()
    return {'message': f'max temperature for last 24 hour is {weather.temperature} at {weather.datetime}'}

@router.get('/historical/min')
async def historical_min():
    service = WeatherService(db)
    weather = await service.get_historical_data_min()
    return {'message': f'min temperature for last 24 hour is {weather.temperature} at {weather.datetime}'}
