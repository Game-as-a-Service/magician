import pytest
from domain.player import Player


@pytest.fixture
def player():
    return Player(1, "Bob")


@pytest.mark.parametrize("hp, expected", [(-3, 3), (-10, 0), (1, 6)])
def test_update_hp(player, hp, expected):
    player.update_HP(hp)
    assert player.get_HP() == expected


@pytest.mark.parametrize("score, expected", [(5, 5), (10, 8)])
def test_update_score(player, score, expected):
    player.update_score(score)
    assert player.score == expected


def test_join_game(player):
    player.join_game()
    assert player.joined is True


@pytest.mark.parametrize(
    "spell_name, expected",
    [("fireball", "Bob casts fireball!"), ("blah", "Bob doesn't have blah spell.")],
)
def test_cast_spell(player, spell_name, expected):
    player.spells = ["fireball"]
    assert player.cast_spell(spell_name) == expected


def test_to_dict(player):
    player_dict = player.to_dict()
    expected = {
        "player_id": 1,
        "name": "Bob",
        "joined": False,
        "score": 0,
        "HP": 6,
        "prev_spell": None,
        "spells": [],
        "secret_spells": [],
    }
    assert player_dict == expected


def test_from_dict():
    player_dict = {"player_id": 1, "name": "Bob"}
    player = Player.from_dict(player_dict)
    assert player.player_id == 1
    assert player.name == "Bob"
