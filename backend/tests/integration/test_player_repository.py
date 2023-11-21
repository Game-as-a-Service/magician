import pytest
from app.config import TestingConfig
from repository.player_repository import PlayerRepository
from domain.player import Player


@pytest.fixture
def repo():
    return PlayerRepository(db_name=TestingConfig.MONGODB_SETTINGS["db"])


def test_create_player(repo):
    player = Player(1, "Alice")

    player_id = repo.create_player(player)

    assert player_id is not None


def test_get_player_by_id(repo):
    player = Player(1, "Alice")
    repo.create_player(player)

    result = repo.get_player_by_id(1)
    assert result.name == "Alice"


def test_get_player_by_id_not_found(repo):
    result = repo.get_player_by_id(666)
    assert result is None
