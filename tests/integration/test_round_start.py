import random
from magician.repository.playerclass import Player_repository


def test_hand_stone():
    hand_stone = [1, 2, 3, 4, 5]
    player = "Yock"
    player_hand_stone = Player_repository(player)
    player_hand_stone.set_player_hand_stone(hand_stone)

    assert player_hand_stone.get_player_hand_stone() == hand_stone
