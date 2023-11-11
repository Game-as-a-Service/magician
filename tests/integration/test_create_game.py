from magician.repository.player_class import Player_repository


def test_players_name():
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player in except_input_name:
        players = Player_repository(player_name = player)
        players.player_name = player
        players.group_names = except_input_name
        assert players.player_name == player
        assert players.group_names == except_input_name

def test_players_seat():
    except_input_seat = [0, 1, 2, 3, 4]
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player, seat in zip(except_input_name, except_input_seat):
        player_seat = Player_repository(player)
        player_seat.player_seat = seat
        assert player_seat.player_seat == seat

    player_seat = Player_repository(except_group_name=except_input_name)
    assert player_seat.get_all_players_seat == except_input_seat


def test_players_HP():
    except_input_hp = [6] * 5
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player, hp in zip(except_input_name, except_input_hp):
        player_hp = Player_repository(player)
        player_hp.player_hp = hp
        assert player_hp.player_hp == hp

    player_hp = Player_repository(except_group_name=except_input_name)
    assert player_hp.get_all_players_hp == except_input_hp


def test_players_score():
    except_input_score = [0] * 5
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player, score in zip(except_input_name, except_input_score):
        player_score = Player_repository(player)
        player_score.player_score = score
        assert player_score.player_score == score

    player_score = Player_repository(except_group_name=except_input_name)
    assert player_score.get_all_players_score == except_input_score

def test_players_handstone():
    except_input_hand_stone = [
        [3, 3, 5, 7, 8],
        [5, 5, 7, 8, 8],
        [4, 5, 5, 6, 8],
        [4, 6, 6, 7, 8],
        [2, 6, 7, 7, 8],
    ]
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player,hand_stone in zip(except_input_name,except_input_hand_stone):
        player_hand_stone = Player_repository(player)
        player_hand_stone.player_hand_stone = hand_stone
        assert player_hand_stone.player_hand_stone == hand_stone

    player_hand_stone = Player_repository(except_group_name=except_input_name)
    assert player_hand_stone.get_all_players_hand_stone == except_input_hand_stone