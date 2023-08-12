def test_spelling_magic3(app, client):
    params = {
        "playerID": "a",
        "stoneID": "magic3",
    }
    res = client.patch("/stone", json=params)

    assert res.status_code == 200

    assert res.json["msg"] == "magic3"


def test_spelling_not_exist_magic9(app, client):
    params = {
        "playerID": "a",
        "stoneID": "magic9",
    }
    res = client.patch("/stone", json=params)

    # Todo: 尚未實作
    # assert res.status_code == 400

    # assert res.json["msg"] == "magic dosen't exist"
