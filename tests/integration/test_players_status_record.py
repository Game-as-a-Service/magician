from magician.repository.playerclass import Player_repository


def test_players_status_record():
    except_input = ["yock", "Teds", "Tux", "Leave3310", "Momo"]
    # except_input_seat = ["A", "B", "C", "D", "E"]
    # seat = ['A','B','C','D','E']

    for player in except_input:
        player_some = Player_repository(player, except_input)
        # player_some.assign_room(except_input)

        # player = player_status(player)
    assert player_some.get_all_player_names() == except_input
    # assert player == ["yock", "Teds", "Tux", "Leave3310", "Momo"]


# def test_players_other_status_record():
#     except_input = ["p1", "p2", "p3", "p4", "p5"]
#     # seat = ['A','B','C','D','E']

#     for player in except_input:
#         player_some = Player(player)

#         # player = player_status(player)
#     assert player_some.get_all_player_names() == except_input
