from tests.integration.happy_path.utiles import game_service, five_player_game


def test_happy_path_round2(game_service, five_player_game, monkeypatch):
    dice_results = [1, 2, 3, 1]

    def mock_roll_dice():
        result = dice_results.pop(0)
        # 使用pytest時
        # 要看到以下除錯用訊息
        # 需加上參數
        # pytest  -o log_cli=true <tests_path>\test_happy_path_round3.py
        print("mock_roll_dice: ", result)
        return result

    monkeypatch.setattr("domain.spell.roll_dice", mock_roll_dice)

    game_id = five_player_game.game_id
    for player in five_player_game.players:
        assert game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)

    # 洗牌 O列
    assert game.turn == 1
    game.round = 2
    game.players[0].score = 0
    game.players[1].score = 1
    game.players[2].score = 2
    game.players[3].score = 1
    game.players[4].score = 1
    game.players[0].spells = ["Magic 4", "Magic 6", "Magic 7", "Magic 7", "Magic 7"]
    game.players[1].spells = ["Magic 1", "Magic 2", "Magic 5", "Magic 5", "Magic 7"]
    game.players[2].spells = ["Magic 5", "Magic 6", "Magic 6", "Magic 7", "Magic 8"]
    game.players[3].spells = ["Magic 4", "Magic 6", "Magic 7", "Magic 8", "Magic 8"]
    game.players[4].spells = ["Magic 3", "Magic 3", "Magic 8", "Magic 8", "Magic 8"]

    game.secret_warehouse = ["Magic 4", "Magic 3", "Magic 2", "Magic 5"]
    game.warehouse = [
        "Magic 5",
        "Magic 6",
        "Magic 8",
        "Magic 7",
        "Magic 8",
        "Magic 4",
        "Magic 6",
    ]

    game_service.game_repository.update_game(game)

    # A施法5 P列
    assert game.round == 2
    assert game.current_player == 0
    game_service.cast_spell(game_id, "A", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 5

    # B施法1 Q列
    assert game.current_player == 1
    assert game.turn == 2
    game_service.cast_spell(game_id, "B", "Magic 1")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("B").spells) == 4
    assert game.find_player_by_id("A").get_HP() == 4
    assert game.find_player_by_id("C").get_HP() == 4
    assert game.find_player_by_id("D").get_HP() == 3
    assert game.find_player_by_id("E").get_HP() == 5
    assert len(game.ladder) == 1

    # B施法2 R列
    game_service.cast_spell(game_id, "B", "Magic 2")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("B").spells) == 3
    assert game.find_player_by_id("A").get_HP() == 3
    assert game.find_player_by_id("C").get_HP() == 3
    assert game.find_player_by_id("D").get_HP() == 2
    assert game.find_player_by_id("E").get_HP() == 4
    assert len(game.ladder) == 2

    # B施法5 S列
    game_service.cast_spell(game_id, "B", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("B").spells) == 2
    assert game.find_player_by_id("A").get_HP() == 2
    assert game.find_player_by_id("C").get_HP() == 2
    assert len(game.ladder) == 3

    # B施法5 T列
    game_service.cast_spell(game_id, "B", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("B").spells) == 1
    assert game.find_player_by_id("A").get_HP() == 1
    assert game.find_player_by_id("C").get_HP() == 1
    assert len(game.ladder) == 4

    # B施法7, 殺死玩家A,將自動進行結算 U列
    game_service.cast_spell(game_id, "B", "Magic 7")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").score == 0
    assert game.find_player_by_id("B").score == 4
    assert game.find_player_by_id("C").score == 2
    assert game.find_player_by_id("D").score == 1
    assert game.find_player_by_id("E").score == 1
