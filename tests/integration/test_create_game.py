from magician.repository.playerclass import Player_repository

def test_players_name():
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player in except_input_name:
        players = Player_repository(player,except_input_name)
        players.set_player_name()

    assert players.get_player_names() == except_input_name


def test_players_seat():
    except_input_seat = [0,1,2,3,4]
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player,seat in zip(except_input_name,except_input_seat):
        player_seat = Player_repository(player)
        player_seat.set_players_seat(seat)

    assert player_seat.get_players_seat(except_input_name) == except_input_seat


def test_players_HP():
    except_input_hp = [6]*5
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player,hp in zip(except_input_name,except_input_hp):
        player_hp = Player_repository(player)
        player_hp.set_players_hp(hp)

    assert player_hp.get_players_hp(except_input_name) == except_input_hp


def test_players_score():
    except_input_score = [0]*5
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player,score in zip(except_input_name,except_input_score):
        player_score = Player_repository(player)
        player_score.set_players_score(score)

    assert player_score.get_players_score(except_input_name) == except_input_score