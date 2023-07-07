import json


def test_hello(app, client):
    res = client.get('/hello')
    assert res.status_code == 200
    expected = {'msg': 'hello world'}
    assert expected == json.loads(res.get_data(as_text=True))
