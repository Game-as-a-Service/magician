import os
from .config import ProductionConfig
from service.game_service import GameService as GameServiceClass
from service.player_service import PlayerService as PlayerServiceClass
from repository.event_emitter import EventEmitter
from repository.data_loader import DataLoader
from repository.game_repository import GameRepository
from repository.player_repository import PlayerRepository
import logging

# 設定log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    emitter = EventEmitter()
    if os.environ.get("MONGO_DB_NAME") is None:
        game_repository = GameRepository()
        player_repository = PlayerRepository()
    else:
        game_repository = GameRepository(
            db_name=ProductionConfig.MONGODB_SETTINGS["db"], emitter=emitter
        )
        player_repository = PlayerRepository(
            db_name=ProductionConfig.MONGODB_SETTINGS["db"]
        )

    loader = DataLoader(emitter=emitter, repo=game_repository)

except Exception as e:
    logger.error(f"Error creating repository instances: {e}")
    raise

try:
    GameService = GameServiceClass(game_repository)
    PlayerService = PlayerServiceClass(player_repository)
except Exception as e:
    logger.error(f"Error creating service instances: {e}")
    raise
