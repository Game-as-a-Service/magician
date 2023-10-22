import random
from magician.repository.playerclass import Player_repository
def test_hand_stone():
#for i in range(1,9):
#    [i] * i

    hand_stone = [1,2,3,4,5]
    player ="Yock"
    player_hand_stone = Player_repository(player)
    player_hand_stone.set_player_hand_stone(hand_stone) #set_hand_stone
    
    assert player_hand_stone.get_hand_stone() == hand_stone


