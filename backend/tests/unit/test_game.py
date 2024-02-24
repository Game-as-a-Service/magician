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


def test_real_game_can_see(game):
    game.players[0].spells = ["Magic 3", "Magic 3", "Magic 5", "Magic 7", "Magic 8"]
    game.players[1].spells = ["Magic 5", "Magic 5", "Magic 7", "Magic 8", "Magic 8"]
    game.players[2].spells = ["Magic 4", "Magic 5", "Magic 5", "Magic 6", "Magic 8"]
    game.players[3].spells = ["Magic 4", "Magic 6", "Magic 6", "Magic 7", "Magic 8"]
    game.players[4].spells = ["Magic 2", "Magic 6", "Magic 7", "Magic 7", "Magic 8"]

    game.secret_warehouse = ["Magic 2", "Magic 3", "Magic 7", "Magic 8"]
    game.warehouse = [
        "Magic 4",
        "Magic 8",
        "Magic 6",
        "Magic 1",
        "Magic 6",
        "Magic 7",
        "Magic 4",
    ]

    player_view = game.real_game_can_see(1)

    # 檢查所有玩家應該可正常檢視部份
    assert player_view.players[0].name == "Yock"
    assert player_view.players[1].name == "Teds"

    assert player_view.players[0].score == 0
    assert player_view.players[1].score == 0

    # 檢查針對玩家編號1隱藏部份
    assert player_view.players[0].spells == ["Magic Stone"] * len(
        game.players[0].spells
    )
    assert player_view.secret_warehouse == ["Magic Stone"] * len(game.secret_warehouse)
    assert player_view.warehouse == ["Magic Stone"] * len(game.warehouse)

    # 檢查針對玩家編號1顯示部份
    assert len(player_view.players[1].spells) == len(game.players[1].spells)
    assert len(player_view.players[2].spells) == len(game.players[2].spells)
    assert len(player_view.players[3].spells) == len(game.players[3].spells)
    assert len(player_view.players[4].spells) == len(game.players[4].spells)


def test_shuffle_player(game):
    game.shuffle_player()
    assert game.current_player >= 0 and game.current_player < 5


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
