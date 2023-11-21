from bson.objectid import ObjectId
from app.extensions import mongo_client
from app.config import DevelopmentConfig
from domain.game import Game


class GameRepository:
    def __init__(self, db_name=DevelopmentConfig.MONGODB_SETTINGS["db"]):
        # 讀取 config 中的設定
        self.collection = mongo_client[db_name]["games"]

    def create_game(self, game):
        """將Game class新增到資料庫"""
        game_dict = game.to_dict()
        result = self.collection.insert_one(game_dict)
        return result.inserted_id

    def get_game_by_id(self, game_id):
        """根據遊戲 ID 從資料庫取得Game class"""
        if not ObjectId.is_valid(game_id):
            return None

        game_data = self.collection.find_one({"_id": ObjectId(game_id)})

        if game_data:
            return Game.from_dict(game_data)
        return None

    def update_game(self, game):
        """更新資料庫中的遊戲記錄"""
        with mongo_client.start_session() as session:
            result = self.collection.update_one(
                {"_id": ObjectId(game.game_id)},
                {"$set": game.to_dict()},
                session=session,
            )
        return result.modified_count > 0

    def delete_game(self, game_id):
        """從資料庫刪除遊戲記錄"""
        result = self.collection.delete_one({"_id": ObjectId(game_id)})
        return result.deleted_count > 0
