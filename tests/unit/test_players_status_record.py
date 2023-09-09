from magician.repository.player import player_status


def test_players_status_record():
    except_input = ["yock", "Teds", "Tux", "Leave3310", "Momo"]
    # seat = ['A','B','C','D','E']

    for player in except_input:
        player = player_status(player)

    assert player == ["yock", "Teds", "Tux", "Leave3310", "Momo"]
