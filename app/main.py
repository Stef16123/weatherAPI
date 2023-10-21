from dotenv import load_dotenv
from fastapi import FastAPI
from routers.weather import router as weather_router

load_dotenv()

app = FastAPI()

app.include_router(weather_router)
