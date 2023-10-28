from magician.repository.playerclass import Player_repository


def test_players_status_record():
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player_name in except_input_name:
        player = Player_repository(player_name, except_input_name)
        player.set_player_name()

    assert player.get_group_names() == except_input_name
