import os


class Config:
    """基礎配置類"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "very-very-secret"
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {  # MongoDB 的配置
        "db": "your_database",
        "host": "localhost",
        "port": 27017,
    }

    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = None
    REDIS_PROTOCOL = "redis"


class DevelopmentConfig(Config):
    """開發環境專用配置"""

    DEBUG = True
    MONGODB_SETTINGS = {"db": "dev_database", "host": "localhost", "port": 27017}


class TestingConfig(Config):
    """測試環境專用配置"""

    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {"db": "test_database", "host": "localhost", "port": 27017}


class ProductionConfig(Config):
    """生產環境專用配置"""

    MONGODB_SETTINGS = {
        "db": os.environ.get("MONGO_DB_NAME") or "prod_database",
        "host": os.environ.get("MONGO_HOST") or "localhost",
        "port": os.environ.get("MONGO_PORT") or 27017,
        "username": os.environ.get("MONGO_USERNAME"),
        "password": os.environ.get("MONGO_PASSWORD"),
    }

    REDIS_HOST = os.environ.get("REDIS_HOST") or "localhost"
    REDIS_PORT = os.environ.get("REDIS_PORT") or 6379
    REDIS_DB = os.environ.get("REDIS_DB") or 0
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or None
    REDIS_PROTOCOL = os.environ.get("REDIS_PROTOCOL") or "redis"
