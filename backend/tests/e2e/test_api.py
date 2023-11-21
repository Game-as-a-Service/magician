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
    data = {"gameRoomID": game_id}
    resp = client.put(f"/player/p1/join", json=data)
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
        # 不然隨機到祕密魔法石就尷尬了
        "spellName": "Magic 6",
    }
    resp = client.patch("/stone", json=cast_spell_data)
    # 不是施法成功(回傳200)就是失敗(回傳400)
    assert resp.status_code in [200, 400]

    player_idx = 0
    # 如果回傳是400，代表施法失敗，輪到下一位玩家施法
    if resp.status_code == 400:
        # 換下一位玩家(第二個玩家)施法
        player_idx = 1
        cast_spell_data["playerID"] = data["playerIDs"][1]
        resp = client.patch("/stone", json=cast_spell_data)

        # 繼續輪流施法，直到成功為止
        while resp.status_code == 400:
            next_player_idx = (
                data["playerIDs"].index(cast_spell_data["playerID"]) + 1
            ) % len(data["playerIDs"])
            cast_spell_data["playerID"] = data["playerIDs"][next_player_idx]
            resp = client.patch("/stone", json=cast_spell_data)
            player_idx = next_player_idx

    # 施法成功,進行[停止施法]測試
    assert resp.status_code == 200

    end_turn_data = {"gameRoomID": game_id, "playerID": data["playerIDs"][player_idx]}

    resp = client.patch(
        "/player/{}/spellstop".format(end_turn_data["playerID"]), json=end_turn_data
    )
    assert resp.status_code == 200
