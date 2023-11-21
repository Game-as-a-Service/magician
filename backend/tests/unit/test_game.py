import pytest
from domain.game import Game
from domain.player import Player
from domain.spell import Spell


@pytest.fixture
def game():
    players = [
        {"player_id": 1, "name": "Yock"},
        {"player_id": 2, "name": "Teds"},
        {"player_id": 3, "name": "Tux"},
        {"player_id": 4, "name": "Leave3310"},
        {"player_id": 5, "name": "Momo"},
    ]
    return Game(1, players)


def test_find_player_by_id(game):
    player = game.find_player_by_id(2)
    assert player.name == "Teds"

    missing = game.find_player_by_id(666)
    assert missing is None


def test_cast_spell(game):
    player = Player(1, "Yock")
    game.players = [player]

    # 這邊是故意用不存在的魔法石
    # 若要使用存在的魔法石去施法
    # 就需要建構完整的遊戲架構
    # 這部份將在GameService那邊進行測試
    spell_name = "Magic No1"

    spell = Spell(spell_name)
    game.spells[spell_name] = spell

    result = game.cast_spell(1, spell_name)

    assert result == spell.cast(game, player)


def test_get_adjacent_players(game):
    assert game.get_left_player(game.players[0]) == game.players[1]
    assert game.get_right_player(game.players[0]) == game.players[4]

    assert game.get_left_player(game.players[2]) == game.players[3]
    assert game.get_right_player(game.players[2]) == game.players[1]

    assert game.get_left_player(game.players[4]) == game.players[0]
    assert game.get_right_player(game.players[4]) == game.players[3]


def test_to_dict(game):
    data = game.to_dict()

    assert data["game_id"] == 1
    assert len(data["players"]) == 5
    assert data["active"] is True


def test_from_dict():
    data = {
        "game_id": 1,
        "players": [
            {"player_id": 1, "name": "Yock"},
            {"player_id": 2, "name": "Teds"},
            {"player_id": 3, "name": "Tux"},
            {"player_id": 4, "name": "Leave3310"},
            {"player_id": 5, "name": "Momo"},
        ],
    }

    game = Game.from_dict(data)

    assert game.game_id == 1
    assert len(game.players) == 5
    assert game.players[0].name == "Yock"
    assert game.players[1].name == "Teds"
    assert game.players[2].name == "Tux"
    assert game.players[3].name == "Leave3310"
    assert game.players[4].name == "Momo"
