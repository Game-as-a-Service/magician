import time
from magician.service.round_start import round_start


def game_create(players):
    if len(players["playerIDs"]) <= 3:
        return "players is not enough"
    elif len(players["playerIDs"]) >= 6:
        return "players is over 5"
    else:
        create_room_id(players["playerIDs"][0])
        round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
