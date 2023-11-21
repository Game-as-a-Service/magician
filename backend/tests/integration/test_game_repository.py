import pytest


from domain.game import Game
from app.config import TestingConfig
from repository.game_repository import GameRepository


@pytest.fixture
def repo():
    return GameRepository(db_name=TestingConfig.MONGODB_SETTINGS["db"])


def test_create_game(repo):
    players = ["Player1", "Player2", "Player3", "Player4", "Player5"]
    game = Game(1, players)

    game_id = repo.create_game(game)

    assert game_id is not None

    repo.get_game_by_id(game.game_id)
    assert len(game.players) == 5
    assert repo.delete_game(game_id) > 0


def test_get_game_by_id_not_found(repo):
    result = repo.get_game_by_id("1234")
    assert result is None


def test_get_game_not_found(repo):
    game = repo.get_game_by_id("1234")
    assert game is None
