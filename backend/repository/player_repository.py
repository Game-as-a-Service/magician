from app.extensions import mongo_client
from app.config import DevelopmentConfig
from domain.player import Player


class PlayerRepository:
    def __init__(self, db_name=DevelopmentConfig.MONGODB_SETTINGS["db"]):
        # 讀取 config 中的設定
        collection_name = "players"

        db = mongo_client[db_name]
        self.collection = db[collection_name]

    def create_player(self, player):
        """將玩家class新增到資料庫"""
        player_dict = player.to_dict()
        result = self.collection.insert_one(player_dict)
        return result.inserted_id

    def get_player_by_id(self, player_id):
        """根據玩家ID 從資料庫取得Player class"""
        player_data = self.collection.find_one({"player_id": player_id})
        if player_data:
            return Player.from_dict(player_data)
        return None
