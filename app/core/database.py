import logging
from interfaces.database import Database
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDatabase(Database):
    db_name: str
    client: AsyncIOMotorClient
    db_url: str 
    username: str
    password: str

    def __init__(self, db_name, db_url, username, password) -> None:
        self.db_name = db_name
        self.db_url = db_url
        self.username = username
        self.password = password

    async def set_db(self):
        try:
            self.client = AsyncIOMotorClient(
                self.db_url,
                username=self.username,
                password=self.password
            )
            self.manager = self.client[self.db_name]
        except Exception as e:
            logging.info(f'Could not connect to mongo: {e}')
            raise

    async def close(self) -> None:
        logging.info("closing connection...")
        self.client.close()
        logging.info("closed connection")
