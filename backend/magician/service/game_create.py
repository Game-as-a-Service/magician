import time
from magician.service.round_start import round_start
from magician.repository.playerclass import Player_repository


def game_create(players):
    players_number = len(players)
    if players_number <= 3:
        return "players is not enough"
    elif players_number >= 6:
        return "players is over 5"
    else:
        except_input_seat = list(range(players_number))
        except_input_HP = [6]*players_number
        except_input_score = [0]*players_number
        
        for player in players:
            player_name = Player_repository(player,players)
            player_name.set_player_name()

        for player,seat in zip(players,except_input_seat):
            player_seat = Player_repository(player)
            player_seat.set_players_seat(seat)

        for player,hp in zip(players,except_input_HP):
            player_hp = Player_repository(player)
            player_hp.set_players_hp(hp)

        for player,score in zip(players,except_input_score):
            player_score = Player_repository(player)
            player_score.set_players_score(score)
        
        create_room_id(players[0])
        #round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
