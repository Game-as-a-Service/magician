def test_create_game(client):
    data = {"playerIDs": ["p1", "p2", "p3", "p4"]}
    resp = client.post("/gameCreate", json=data)

    assert resp.status_code == 201
    assert "gameRoomID" in resp.json


def test_create_game_invalid_data(client):
    # Too few players
    data = {"playerIDs": ["p1", "p2"]}
    resp = client.post("/gameCreate", json=data)
    assert resp.status_code == 400

    # Too many players
    data = {"playerIDs": ["p1", "p2", "p3", "p4", "p5", "p6"]}
    resp = client.post("/gameCreate", json=data)
    assert resp.status_code == 400

    # No playerIDs
    data = {"data": "other data"}
    resp = client.post("/gameCreate", json=data)
    assert resp.status_code == 400


def test_player_join_game(client):
    # Create game
    data = {"playerIDs": ["p1", "p2", "p3", "p4", "p5"]}
    resp = client.post("/gameCreate", json=data)
    game_id = resp.json["gameRoomID"]

    # Player join game
    game_id_data = {"gameRoomID": game_id}
    resp = client.put(f"/player/{data['playerIDs'][0]}/join", json=game_id_data)
    assert resp.status_code == 200

    # Verify player joined
    data = resp.json
    assert data["message"] == "Player joined the game"
    assert data["gameRoomID"] == game_id


def test_player_cast_spell(client):
    # 建立遊戲房間
    data = {"playerIDs": ["p1", "p2", "p3", "p4", "p5"]}
    resp = client.post("/gameCreate", json=data)
    game_id = resp.json["gameRoomID"]

    # 所有玩家都已經準備就緒
    gameRoomID_data = {"gameRoomID": game_id}
    for player_id in data["playerIDs"]:
        resp = client.put("/player/{}/join".format(player_id), json=gameRoomID_data)
        assert resp.status_code == 200

    # 第一個玩家施法
    cast_spell_data = {
        "gameRoomID": game_id,
        "playerID": data["playerIDs"][0],
        # 這邊的測試魔法石要選數量多的
        "spellName": "Magic 6",
    }
    resp = client.patch("/stone", json=cast_spell_data)
    resp_data = resp.json
    assert "message" in resp_data

    player_idx = 0
    # 如果回傳是"Spell cast failed"，代表施法失敗，輪到下一位玩家施法
    if resp.status_code == 200 and resp_data["message"] == "Spell cast failed":
        # 換下一位玩家(第二個玩家)施法
        player_idx = 1
        cast_spell_data["playerID"] = data["playerIDs"][player_idx]
        resp = client.patch("/stone", json=cast_spell_data)
        resp_data = resp.json
        # 繼續輪流施法，直到成功為止
        while not (
            resp.status_code == 200
            and resp_data["message"] == "Spell cast successfully"
        ):
            next_player_idx = (
                data["playerIDs"].index(cast_spell_data["playerID"]) + 1
            ) % len(data["playerIDs"])
            cast_spell_data["playerID"] = data["playerIDs"][next_player_idx]
            resp = client.patch("/stone", json=cast_spell_data)
            resp_data = resp.json
            player_idx = next_player_idx

    # 施法成功,進行[停止施法]測試
    assert resp_data["message"] == "Spell cast successfully"

    end_turn_data = {"gameRoomID": game_id, "playerID": data["playerIDs"][player_idx]}

    resp = client.patch(
        "/player/{}/spellstop".format(end_turn_data["playerID"]), json=end_turn_data
    )
    assert resp.status_code == 200


def test_roomID_status(client):
    # Create game
    data = {"playerIDs": ["p1", "p2", "p3", "p4", "p5"]}
    resp = client.post("/gameCreate", json=data)
    game_id = resp.json["gameRoomID"]

    # Player join game
    game_id_data = {"gameRoomID": game_id}
    resp = client.put(f"/player/{data['playerIDs'][0]}/join", json=game_id_data)
    assert resp.status_code == 200

    # 測試gameRoomID 與 player_id 正確
    params = "player_id=p1&gameRoomID=" + game_id
    resp = client.get(f"/player/status?{params}")
    assert resp.status_code == 200

    # 測試gameRoomID不存在 與 player_id 正確
    params = "player_id=p1"    
    resp = client.get(f"/player/status?{params}")    
    assert resp.status_code == 400
    resp_json = resp.json
    assert resp_json["message"] == "gameRoomID not found"

    # 測試gameRoomID錯誤的 與 player_id 正確
    params = "player_id=p1&gameRoomID=" + "wrong_gameroomID"
    resp = client.get(f"/player/status?{params}")    
    assert resp.status_code == 400
    resp_json = resp.json
    assert resp_json["message"] == "gameRoomID does not exist"

    # 測試gameRoomID正確 與 player_id 不存在
    params = "gameRoomID=" + game_id
    resp = client.get(f"/player/status?{params}")    
    assert resp.status_code == 400
    resp_json = resp.json
    assert resp_json["message"] == "player_id not found"