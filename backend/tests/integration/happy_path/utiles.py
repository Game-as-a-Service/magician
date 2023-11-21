import pytest
from app.config import TestingConfig
from repository.game_repository import GameRepository
from service.game_service import GameService as GameServiceClass


@pytest.fixture(scope="function")
def game_service():
    game_repository = GameRepository(db_name=TestingConfig.MONGODB_SETTINGS["db"])
    game_service = GameServiceClass(game_repository)
    return game_service


@pytest.fixture(scope="function")
def five_player_game(game_service):
    player_ids = [
        "A",
        "B",
        "C",
        "D",
        "E",
    ]
    five_player_game = game_service.create_game(player_ids)

    yield five_player_game

    game_service.game_repository.delete_game(five_player_game.game_id)
