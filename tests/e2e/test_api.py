import json


def test_hello(app, client):
    res = client.get('/hello')
    assert res.status_code == 200
    expected = {'msg': 'hello world'}
    assert expected == json.loads(res.get_data(as_text=True))


# TODO遊戲人數5人
# 開始遊戲
def test_game_create_success(app, client):
    expected = {"playerIDs": ["Teds", "Tux", "Yock", "Momo", "Leave3310"]}
    # expected = {'playerIDs': [
    # {"id":"Teds"},
    # {"id":"Tux"},
    # {"id":"Yock"},
    # {"id":"Momo"},
    # {"id":"Leave3310"},
    # ]}
    res = client.post('/gameCreate', json=expected)
    assert res.status_code == 201


def test_game_create_is_less_than_4_players(app, client):
    expected = {"playerIDs": ["Teds", "Tux", "Yock"]}
    res = client.post('/gameCreate', json=expected)
    assert res.status_code == 400


def test_game_create_more_than_5_players(app, client):
    expected = {"playerIDs": ["Teds", "Tux", "Yock", "Momo", "Leave3310","dn"]}
    res = client.post('/gameCreate', json=expected)
    assert res.status_code == 400

# def test_GameJoin_Success():
#     res = client.put('/player/<playerID>/join')    
#     assert res.status_code == 200