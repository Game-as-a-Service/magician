from tests.integration.happy_path.utiles import game_service, five_player_game


def test_happy_path_round1(game_service, five_player_game, monkeypatch):
    dice_results = [3]

    def mock_roll_dice():
        result = dice_results.pop(0)
        # 使用pytest時
        # 要看到以下除錯用訊息
        # 需加上參數
        # pytest  -o log_cli=true <tests_path>\test_happy_path_round3.py
        print("mock_roll_dice: ", result)
        return result

    monkeypatch.setattr("service.game_service.roll_dice", mock_roll_dice)

    game_id = five_player_game.game_id
    for player in five_player_game.players:
        assert game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)

    assert game.round == 1
    assert game.turn == 1

    for i in range(5):
        assert game.players[i].score == 0
        assert game.players[i].get_HP() == 6

    # 洗牌 B列
    game.players[0].spells = ["Magic 3", "Magic 3", "Magic 5", "Magic 7", "Magic 8"]
    game.players[1].spells = ["Magic 5", "Magic 5", "Magic 7", "Magic 8", "Magic 8"]
    game.players[2].spells = ["Magic 4", "Magic 4", "Magic 5", "Magic 6", "Magic 8"]
    game.players[3].spells = ["Magic 5", "Magic 6", "Magic 6", "Magic 7", "Magic 8"]
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

    game_service.game_repository.update_game(game)

    # A施法5 C列
    assert game.current_player == 0
    game_service.cast_spell(game_id, "A", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("B").get_HP() == 5
    assert game.find_player_by_id("E").get_HP() == 5
    assert len(game.find_player_by_id("A").spells) == 4
    assert len(game.ladder) == 1

    # A施法6(施法失敗，系統自動補充手牌) D列
    assert game.current_player == 0
    game_service.cast_spell(game_id, "A", "Magic 6")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 5
    assert game.find_player_by_id("A").spells[4] == "Magic 4"
    assert len(game.warehouse) == 6

    # B施法5 F列
    assert game.current_player == 1
    assert game.turn == 2
    game_service.cast_spell(game_id, "B", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 4
    assert game.find_player_by_id("C").get_HP() == 5
    assert len(game.find_player_by_id("B").spells) == 4
    assert len(game.ladder) == 2

    # B施法5 G列
    assert game.current_player == 1
    game_service.cast_spell(game_id, "B", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 3
    assert game.find_player_by_id("C").get_HP() == 4
    assert len(game.find_player_by_id("B").spells) == 3
    assert len(game.ladder) == 3

    # B補充手牌5 H列
    assert game.current_player == 1
    assert game_service.end_turn(game_id, "B")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("B").spells[3] == "Magic 7"
    assert game.find_player_by_id("B").spells[4] == "Magic 6"
    assert len(game.warehouse) == 4

    # C施法4 I列
    assert game.current_player == 2
    assert game.turn == 3
    game_service.cast_spell(game_id, "C", "Magic 4")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("C").spells) == 4
    assert game.find_player_by_id("C").secret_spells[0] == "Magic 8"
    assert len(game.secret_warehouse) == 3
    assert len(game.ladder) == 4

    # C施法4 J列
    assert game.current_player == 2
    assert game.turn == 3
    game_service.cast_spell(game_id, "C", "Magic 4")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("C").spells) == 3
    assert game.find_player_by_id("C").secret_spells[1] == "Magic 7"
    assert len(game.secret_warehouse) == 2
    assert len(game.ladder) == 5

    # C補充手牌5 K列
    assert game.current_player == 2
    assert game_service.end_turn(game_id, "C")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("C").spells[3] == "Magic 1"
    assert game.find_player_by_id("C").spells[4] == "Magic 6"
    assert len(game.warehouse) == 2

    # D施法5 L列
    assert game.current_player == 3
    assert game.turn == 4
    game_service.cast_spell(game_id, "D", "Magic 3")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("D").get_HP() == 5

    # E施法5 M列
    assert game.current_player == 4
    assert game.turn == 5
    game_service.cast_spell(game_id, "E", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("E").get_HP() == 4

    # A施法1, 因為玩家A自殺, 自動進入結算 N列
    assert game.current_player == 0
    assert game.turn == 6
    game_service.cast_spell(game_id, "A", "Magic 1")
    game = game_service.game_repository.get_game_by_id(game_id)
    for player in game.players:
        assert player.get_HP() == 6
    assert game.find_player_by_id("A").score == 0
    assert game.find_player_by_id("B").score == 1
    assert game.find_player_by_id("C").score == 3
    assert game.find_player_by_id("D").score == 1
    assert game.find_player_by_id("E").score == 1
