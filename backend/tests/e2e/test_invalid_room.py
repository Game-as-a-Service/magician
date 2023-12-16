def test_player_somebody_not_ready(client):
    # 建立遊戲房間
    data = {"playerIDs": ["p1", "p2", "p3", "p4", "p5"]}
    resp = client.post("/gameCreate", json=data)
    game_id = resp.json["gameRoomID"]

    # 只有一位玩家準備就緒
    gameRoomID_data = {"gameRoomID": game_id}
    resp = client.put("/player/p1/join", json=gameRoomID_data)
    assert resp.status_code == 200

    # 第一個玩家施法
    cast_spell_data = {
        "gameRoomID": game_id,
        "playerID": data["playerIDs"][0],
        "spellName": "Magic 6",
    }
    resp = client.patch("/stone", json=cast_spell_data)
    assert resp.status_code == 400

    # 第一個玩家停止施法
    resp = client.patch(
        "/player/{}/spellstop".format(data["playerIDs"][0]), json=gameRoomID_data
    )
    assert resp.status_code == 400

    # 第二個玩家施法
    cast_spell_data = {
        "gameRoomID": game_id,
        "playerID": data["playerIDs"][1],
        "spellName": "Magic 6",
    }
    resp = client.patch("/stone", json=cast_spell_data)
    assert resp.status_code == 400

    # 第二個玩家停止施法
    resp = client.patch(
        "/player/{}/spellstop".format(data["playerIDs"][1]), json=gameRoomID_data
    )
    assert resp.status_code == 400
