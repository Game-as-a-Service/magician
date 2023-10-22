from magician.service.game_create import game_create


def test_game_create():
    except_input = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]
    assert "start game" == game_create(except_input)


def test_game_cant_create_less_than_4_players():
    except_input = ["Teds", "Tux"]
    assert "players is not enough" == game_create(except_input)


def test_game_cant_create_more_than_5_players():
    except_input = ["Teds", "Tux", "Yock", "Momo", "Leave3310", "dn"]
    assert "players is over 5" == game_create(except_input)
