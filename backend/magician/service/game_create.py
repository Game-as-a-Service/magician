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
        except_input_HP = [6]*5
        except_input_score = [0]*5
        
        for player in players["playerIDs"]:
            player_name = Player_repository(player,players["playerIDs"])
            player_name.set_player_name()        

        for player,seat in zip(players["playerIDs"],except_input_seat):
            player_seat = Player_repository(player)
            player_seat.set_players_seat(seat)        

        for player,hp in zip(players["playerIDs"],except_input_HP):
            player_hp = Player_repository(player)
            player_hp.set_players_hp(hp)        

        for player,score in zip(players["playerIDs"],except_input_score):
            player_score = Player_repository(player)
            player_score.set_players_score(score)    
            
        assert player_name.get_player_names() == players["playerIDs"]
        assert player_seat.get_players_seat(players["playerIDs"]) == except_input_seat
        assert player_hp.get_players_hp(players["playerIDs"]) == except_input_HP
        assert player_score.get_players_score(players["playerIDs"]) == except_input_score
        
        create_room_id(players["playerIDs"][0])
        #round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
