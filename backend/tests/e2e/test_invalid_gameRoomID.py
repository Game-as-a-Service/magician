def test_join_game_invalid_gameRoomID(client):
    game_id_data = {"gameRoomID": "invalid gameRoomID"}
    resp = client.put("/player/p1/join", json=game_id_data)
    assert resp.status_code == 400


def test_stone_invalid_gameRoomID(client):
    game_id_data = {
        "gameRoomID": "invalid gameRoomID",
        "playerID": "p1",
        "spellName": "Magic 1",
    }
    resp = client.patch("/stone", json=game_id_data)
    assert resp.status_code == 400


def test_stop_spell_invalid_gameRoomID(client):
    game_id_data = {"gameRoomID": "invalid gameRoomID"}
    resp = client.patch("/player/p1/spellstop", json=game_id_data)
    assert resp.status_code == 400
