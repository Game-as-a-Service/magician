import time
from magician.service.game_create import create_room_id


def test_create_room_created():
    except_input = "Teds"
    roomID1 = create_room_id(except_input)
    time.sleep(0.0001)
    roomID2 = create_room_id(except_input)
    assert roomID1 != roomID2
