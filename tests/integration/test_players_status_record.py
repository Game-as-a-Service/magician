from magician.repository.player_class import Player_repository


def test_players_status_record():
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player_name in except_input_name:
        player = Player_repository(player_name = player_name)
        player.player_name = player_name
        player.group_names = except_input_name
        assert player.player_name == player_name
        assert player.group_names == except_input_name
