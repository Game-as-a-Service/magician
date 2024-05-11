import os
from socketio import RedisManager
from app.config import Config, DevelopmentConfig, ProductionConfig


class Redis_URI:
    """Redis client configuration"""

    def __init__(self, config: Config):
        self.config: Config = config
        self.host: str = self.config.REDIS_HOST
        self.port: int = self.config.REDIS_PORT
        self.db: int = self.config.REDIS_DB
        self.REDIS_PROTOCOL: str = self.config.REDIS_PROTOCOL
        if self.config.REDIS_PASSWORD:
            self.redis_uri: str = (
                f"{self.REDIS_PROTOCOL}://default:{self.config.REDIS_PASSWORD}@{self.host}:{self.port}/{self.db}"
            )
        else:
            self.redis_uri: str = (
                f"{self.REDIS_PROTOCOL}://{self.host}:{self.port}/{self.db}"
            )
        self.client: RedisManager = RedisManager(self.redis_uri, write_only=True)


def get_redis_manager(app_config: Config) -> RedisManager:
    """Create Redis client from application config"""
    return Redis_URI(app_config).client


if os.environ.get("REDIS_HOST") is None:
    config = DevelopmentConfig()
else:
    config = ProductionConfig()

external_sio: RedisManager = get_redis_manager(config)
