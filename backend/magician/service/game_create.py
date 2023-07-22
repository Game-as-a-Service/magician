
def game_create(players):

    if len(players['playerIDs']) <= 3:
        return 'players is not enough'
    elif len(players['playerIDs']) >= 6 :
        return 'players is over 5'
    else:
        return 'start game'
