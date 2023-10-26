from abc import ABC, abstractmethod


class Database(ABC):
    db_name: str
    client: None
    db_url: str 
    username: str
    password: str

    @abstractmethod
    async def __init__(self, db_name, db_url, username, password) -> None:
        self.db_name = db_name
        self.db_url = db_url
        self.username = username
        self.password = password

    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass