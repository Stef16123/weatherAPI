from typing import Union
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from core.models import Weather
from interfaces.schemas import WeatherList
from core.services import WeatherService
from core.config import db
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)

async def get_db():
    try:
        if not hasattr(db, 'self.manager'):
            await db.set_db()
        s = await db.client.start_session()
        yield db
    finally:
        await s.end_session()

@router.get("/last-hour")
async def get_last_hour(db = Depends(get_db)):
    service = WeatherService(db)
    temperature: Union[int, float, None] = await service.get_last_hour_temperature()
    if not temperature:
        return JSONResponse(
            content={'message': 'weather temperature on the last hour is not found'},
            status_code=404
            )
    return JSONResponse(
        content={'message': f'weather temperature on the last hour is {temperature} C'}, 
        status_code=200
        )

@router.get("/current")
async def get_current(db = Depends(get_db)):
    service = WeatherService(db)
    temperature: Union[int, float, None] = await service.get_current_temperature()
    if not temperature:
        return JSONResponse(
            content={'message': 'current weather temperature is not found'}, 
            status_code=404
            )
    return JSONResponse(
        content={'message': f'current weather temperature is {temperature} C'},
        status_code=200)

@router.get('/historical')
async def get_historical(db = Depends(get_db)):
    service = WeatherService(db)
    hist: Union[list[Weather], list[None]]  =  await service.get_historical_data()
    if not hist:
        return JSONResponse(content={}, status_code=404) 
    return JSONResponse(content=jsonable_encoder(WeatherList(list=hist)), status_code=200) 

@router.get('/historical/max')
async def get_historical_max(db = Depends(get_db)):
    service = WeatherService(db)
    weather: Union[Weather, None] = await service.get_historical_data_max()
    if not weather:
        return JSONResponse(
        content={'message': f'max temperature not found'},
        status_code=404
        )
    return JSONResponse(
        content={'message': f'max temperature for last 24 hour is {weather.temperature} at {weather.datetime}'},
        status_code=200
        )

@router.get('/historical/min')
async def historical_min(db = Depends(get_db)):
    service = WeatherService(db)
    weather: Union[Weather, None] = await service.get_historical_data_min()
    if not weather:
        return JSONResponse(
        content={'message': f'min temperature not found'},
        status_code=404
        )
    return JSONResponse(
        content={'message': f'min temperature for last 24 hour is {weather.temperature} at {weather.datetime}'},
        status_code=200)
