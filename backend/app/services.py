from service.game_service import GameService as GameServiceClass
from service.player_service import PlayerService as PlayerServiceClass
from repository.game_repository import GameRepository
from repository.player_repository import PlayerRepository
import logging

# 設定log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    game_repository = GameRepository()
    player_repository = PlayerRepository()
except Exception as e:
    logger.error(f"Error creating repository instances: {e}")
    raise

try:
    GameService = GameServiceClass(game_repository)
    PlayerService = PlayerServiceClass(player_repository)
except Exception as e:
    logger.error(f"Error creating service instances: {e}")
    raise
