import json
from bson.objectid import ObjectId
from typing import Any, Dict
from .redis_manager import external_sio


class RedisRepository:
    def __init__(self):
        self.external_sio = external_sio

    def publish(self, channel: str, room_id: str, data: Dict[str, Any]) -> None:
        # TODO
        # 與backend\service\game_service.py內的
        # player_status隱函數convert_object_id重複
        # 可合併為utility function
        def convert_object_id(data):
            if isinstance(data, dict):
                for k, v in data.items():
                    data[k] = convert_object_id(v)
            elif isinstance(data, ObjectId):
                return str(data)
            return data

        data = convert_object_id(data)
        json_data = json.dumps(data)
        self.external_sio.emit(channel, data=json_data, room=room_id)
