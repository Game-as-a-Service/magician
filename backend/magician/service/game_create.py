import time
from magician.service.round_start import round_start
from magician.repository.playerclass import Player_repository


def game_create(players):
    players_number = len(players["playerIDs"])
    if players_number <= 3:
        return "players is not enough"
    elif players_number >= 6:
        return "players is over 5"
    else:
        except_input_seat = list(range(players_number))
        except_input_HP = [6]*players_number
        except_input_score = [0]*players_number
        Player_repository(
            players["playerIDs"],
            except_input_seat,
            except_input_HP,
            except_input_score
        )
        create_room_id(players["playerIDs"][0])
        #round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
