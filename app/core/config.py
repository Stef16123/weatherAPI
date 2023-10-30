import os
import aioschedule as schedule
from core.scheduler import Sсheduler
from core.tasks import Task
from core.database import MongoDatabase


API_KEY = os.environ['API_KEY']
MONGO_PORT= os.environ['MONGO_PORT']
MONGO_USER = os.environ['MONGO_INITDB_ROOT_USERNAME']
MONGO_PASS = os.environ['MONGO_INITDB_ROOT_PASSWORD']
MONGO_DB_NAME = os.environ['MONGO_INITDB_DATABASE']

MONGO_DB_URL = f'mongodb://mongodb:{MONGO_PORT}'


db = MongoDatabase(
    db_name=MONGO_DB_NAME,
    db_url=MONGO_DB_URL,
    username=MONGO_USER,
    password=MONGO_PASS
)
tasks = Task(db, API_KEY)

tasks_config = {
     'FETCH_DATA_EVERY_60_MINUTES': {
         'schedule':  schedule.every(1).hours.at(':00').do,
         'task': tasks.fetch_current_data
     }
}

scheduler = Sсheduler(tasks_config)
