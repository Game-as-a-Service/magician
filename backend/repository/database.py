import os
from typing import Union

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.config import Config, DevelopmentConfig, ProductionConfig


class MongoDB:
    """MongoDB database application config"""

    def __init__(self, config: Config):
        self.config: Config = config

        username: Union[str, None] = self.config.MONGODB_SETTINGS.get("username")
        password: Union[str, None] = self.config.MONGODB_SETTINGS.get("password")

        uri: str = (
            f"mongodb://{self.config.MONGODB_SETTINGS['host']}:{self.config.MONGODB_SETTINGS['port']}/?retryWrites=true&w=majority"
        )

        if username and password:
            uri = f"mongodb+srv://{username}:{password}@{self.config.MONGODB_SETTINGS['host']}/"
            uri += "?retryWrites=true&w=majority"

        self.uri: str = uri
        self.client: MongoClient = MongoClient(self.uri, server_api=ServerApi("1"))


def get_database_client(app_config: Config) -> MongoClient:
    """Create MongoDB client from application config"""
    return MongoDB(app_config).client


if os.environ.get("MONGO_DB_NAME") is None:
    config: Config = DevelopmentConfig()
else:
    config: Config = ProductionConfig()

mongo_client = get_database_client(config)
