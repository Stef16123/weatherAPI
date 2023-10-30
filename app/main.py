import asyncio
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from routers.health import router as health
from routers.weather import router as weather
from core.config import db, scheduler


load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    await db.connect()
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler.run())
    yield
    await db.close()

app = FastAPI(lifespan=lifespan)

app.include_router(weather)
app.include_router(health)
