from tests.integration.happy_path.utiles import game_service, five_player_game


def test_happy_path_round4(game_service, five_player_game):
    game_id = five_player_game.game_id
    for player in five_player_game.players:
        assert game_service.player_join_game(game_id, player.player_id)

    game = game_service.game_repository.get_game_by_id(game_id)

    # 洗牌 AF列
    assert game.turn == 1
    game.round = 4
    game.players[0].score = 0
    game.players[1].score = 5
    game.players[2].score = 3
    game.players[3].score = 2
    game.players[4].score = 4
    game.players[0].spells = ["Magic 2", "Magic 3", "Magic 6", "Magic 7", "Magic 8"]
    game.players[1].spells = ["Magic 5", "Magic 6", "Magic 6", "Magic 8", "Magic 8"]
    game.players[2].spells = ["Magic 1", "Magic 5", "Magic 7", "Magic 8", "Magic 8"]
    game.players[3].spells = ["Magic 5", "Magic 7", "Magic 7", "Magic 8", "Magic 8"]
    game.players[4].spells = ["Magic 2", "Magic 3", "Magic 5", "Magic 6", "Magic 6"]

    game.secret_warehouse = ["Magic 6", "Magic 4", "Magic 4", "Magic 7"]
    game.warehouse = [
        "Magic 4",
        "Magic 4",
        "Magic 8",
        "Magic 7",
        "Magic 3",
        "Magic 7",
        "Magic 5",
    ]

    game_service.game_repository.update_game(game)

    # A施法5 AG列
    assert game.round == 4
    assert game.turn == 1
    assert game.current_player == 0
    game_service.cast_spell(game_id, "A", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 5

    # B施法5 AH列
    assert game.turn == 2
    assert game.current_player == 1
    game_service.cast_spell(game_id, "B", "Magic 5")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").get_HP() == 4
    assert game.find_player_by_id("C").get_HP() == 5
    assert len(game.find_player_by_id("B").spells) == 4
    assert len(game.ladder) == 1

    # B施法6 AI列
    game_service.cast_spell(game_id, "B", "Magic 6")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("C").get_HP() == 4
    assert len(game.find_player_by_id("B").spells) == 3
    assert len(game.ladder) == 2

    # B施法6 AJ列
    game_service.cast_spell(game_id, "B", "Magic 6")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("C").get_HP() == 3
    assert len(game.find_player_by_id("B").spells) == 2
    assert len(game.ladder) == 3

    # B施法8 AK列
    game_service.cast_spell(game_id, "B", "Magic 8")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert len(game.find_player_by_id("B").spells) == 1
    assert len(game.ladder) == 4

    # B施法8, 玩家將手牌用完, 系統自動結算 AL列
    game_service.cast_spell(game_id, "B", "Magic 8")
    game = game_service.game_repository.get_game_by_id(game_id)
    assert game.find_player_by_id("A").score == 0
    assert game.find_player_by_id("B").score == 8
    assert game.find_player_by_id("C").score == 3
    assert game.find_player_by_id("D").score == 2
    assert game.find_player_by_id("E").score == 4
    # 勝利者出現，遊戲結束
    assert game.active is False
