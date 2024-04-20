import pytest
from app.config import TestingConfig
from domain.spell import Spell
from repository.game_repository import GameRepository
from service.game_service import GameService as GameServiceClass


@pytest.fixture(scope="module")
def game_service():
    game_repository = GameRepository(db_name=TestingConfig.MONGODB_SETTINGS["db"])
    game_service = GameServiceClass(game_repository)
    return game_service


@pytest.fixture(scope="module")
def five_player_game(game_service):
    player_ids = [
        "Yock",
        "Teds",
        "Tux",
        "Leave3310",
        "Momo",
    ]
    five_player_game = game_service.create_game(player_ids)

    yield five_player_game

    game_service.game_repository.delete_game(five_player_game.game_id)


@pytest.fixture(scope="function")
def players(five_player_game):
    return five_player_game.players


def test_create_five_player_game(five_player_game):
    assert len(five_player_game.players) == 5


def test_player_initialize(players):
    player = players[0]

    player.initialize()

    assert player.get_HP() == 6
    assert player.prev_spell is None
    assert player.spells == []
    assert player.secret_spells == []


def test_player_add_score(players):
    player = players[0]
    init_score = player.score

    player.update_score(2)

    assert player.score == init_score + 2


def test_player_reduce_HP(players):
    player = players[0]
    init_HP = player.get_HP()

    damage = -2

    player.update_HP(damage)

    assert player.get_HP() == init_HP + damage


def test_player_cast_spell(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)
    player = game.players[0]
    # 開始遊戲後，玩家手牌必定5張
    assert len(player.spells) == 5
    # 偷看手牌第一張魔法石為何
    spell_name = player.spells[0]
    # 玩家施法-用剛剛的魔法石
    result, status_code = game_service.cast_spell(game_id, player.player_id, spell_name)
    # 施法必定成功
    assert result is True
    assert status_code == 200


def test_spell_fire_dragon(five_player_game, players, monkeypatch):
    dice_results = [2]
    dice_results_iter = iter(dice_results)
    monkeypatch.setattr("domain.spell.roll_dice", lambda: next(dice_results_iter))
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 1")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1
    assert player2.get_HP() == init_HP2 - dice_results[0]
    assert player3.get_HP() == init_HP3 - dice_results[0]
    assert player4.get_HP() == init_HP4 - dice_results[0]
    assert player5.get_HP() == init_HP5 - dice_results[0]


def test_spell_dark_ghost(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    player1.update_HP(-3)

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 2")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1 + 1
    assert player2.get_HP() == init_HP2 - 1
    assert player3.get_HP() == init_HP3 - 1
    assert player4.get_HP() == init_HP4 - 1
    assert player5.get_HP() == init_HP5 - 1


def test_spell_sweet_dream(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    player1.update_HP(-3)

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 3")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() > init_HP1
    assert player2.get_HP() == init_HP2
    assert player3.get_HP() == init_HP3
    assert player4.get_HP() == init_HP4
    assert player5.get_HP() == init_HP5


def test_spell_owl(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)

    player1 = game.players[0]
    spell_name = "Magic 4"
    player1.spells[0] = spell_name
    spell = Spell(spell_name)
    spell.cast(game, player1)

    # 從祕密倉庫取得一張魔法石
    assert len(game.secret_warehouse) == 4 - 1
    # 放入玩家的祕密魔法石列表
    assert len(player1.secret_spells) == 1


def test_spell_lightning_storm(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 5")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1
    assert player2.get_HP() == init_HP2 - 1
    assert player3.get_HP() == init_HP3
    assert player4.get_HP() == init_HP4
    assert player5.get_HP() == init_HP5 - 1


def test_spell_blizzard(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 6")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1
    assert player2.get_HP() == init_HP2 - 1
    assert player3.get_HP() == init_HP3
    assert player4.get_HP() == init_HP4
    assert player5.get_HP() == init_HP5


def test_spell_fireball(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 7")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1
    assert player2.get_HP() == init_HP2
    assert player3.get_HP() == init_HP3
    assert player4.get_HP() == init_HP4
    assert player5.get_HP() == init_HP5 - 1


def test_spell_magic_potion(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    player1.update_HP(-3)

    init_HP1 = player1.get_HP()
    init_HP2 = player2.get_HP()
    init_HP3 = player3.get_HP()
    init_HP4 = player4.get_HP()
    init_HP5 = player5.get_HP()

    spell = Spell("Magic 8")
    spell.cast(five_player_game, player1)

    assert player1.get_HP() == init_HP1 + 1
    assert player2.get_HP() == init_HP2
    assert player3.get_HP() == init_HP3
    assert player4.get_HP() == init_HP4
    assert player5.get_HP() == init_HP5


# 測試左右玩家輪替
def test_left_right_player(five_player_game, players):
    player1 = players[0]
    player2 = players[1]
    player3 = players[2]
    player4 = players[3]
    player5 = players[4]

    left1 = five_player_game.get_left_player(player1)
    right1 = five_player_game.get_right_player(player1)

    assert left1.player_id == player2.player_id
    assert right1.player_id == player5.player_id

    left1 = five_player_game.get_left_player(player5)
    right1 = five_player_game.get_right_player(player5)

    assert left1.player_id == player1.player_id
    assert right1.player_id == player4.player_id

    left1 = five_player_game.get_left_player(player3)
    right1 = five_player_game.get_right_player(player3)

    assert left1.player_id == player4.player_id
    assert right1.player_id == player2.player_id


# 測試是否正確回傳玩家狀態
def test_player_status(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        game_service.player_join_game(game_id, player.player_id)

    query_player_id = five_player_game.players[2].player_id
    assert query_player_id == "Tux"

    game_service_result = game_service.player_status(game_id, query_player_id)
    assert game_service_result["active"]
    assert game_service_result["current_player"] == 0
    assert game_service_result["turn"] == 1
    assert game_service_result["round"] == 1
    assert game_service_result["players"][2]["player_id"] == "Tux"
    assert game_service_result["players"][2]["HP"] == 6

# 測試玩家重複加入，不會開新的一局
def test_player_rejoined(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)
    game.round = 2
    game_service.game_repository.update_game(game)

    assert game_service.player_join_game(game_id, "Yock") == False
    game2 = game_service.game_repository.get_game_by_id(game_id)
    assert game2.round == 2

#取得遊戲狀態若無此房號則回傳訊息
def test_roomID_status(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        game_service.player_join_game(game_id, player.player_id)

    query_player_id = five_player_game.players[2].player_id
    assert query_player_id == "Tux"

    #輸入正確的player_id、錯誤的game_roomID
    room_id = None
    game_roomID = game_service.player_status(room_id, query_player_id)
    assert game_roomID is None
