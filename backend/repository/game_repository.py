from typing import Optional
from bson.objectid import ObjectId
from .database import mongo_client
from app.config import DevelopmentConfig
from domain.game import Game


class GameRepository:
    def __init__(self, db_name: Optional[str] = None, emitter=None):
        # 讀取 config 中的設定
        if db_name is None:
            self.collection = mongo_client[DevelopmentConfig.MONGODB_SETTINGS["db"]][
                "games"
            ]
        else:
            self.collection = mongo_client[db_name]["games"]

        if emitter:
            self.emitter = emitter
        else:
            self.emitter = None

    def create_game(self, game: Game) -> ObjectId:
        """將Game class新增到資料庫"""
        game_dict = game.to_dict()
        result = self.collection.insert_one(game_dict)
        return result.inserted_id

    def get_game_by_id(self, game_id: str) -> Optional[Game]:
        """根據遊戲 ID 從資料庫取得Game class"""
        if not ObjectId.is_valid(game_id):
            return None

        game_data = self.collection.find_one({"_id": ObjectId(game_id)})

        if game_data:
            return Game.from_dict(game_data)
        return None

    def update_game(self, game: Game) -> bool:
        """更新資料庫中的遊戲記錄"""
        with mongo_client.start_session() as session:
            result = self.collection.update_one(
                {"_id": ObjectId(game.game_id)},
                {"$set": game.to_dict()},
                session=session,
            )
        if self.emitter:
            self.emitter.emit("game_updated", game.game_id)
        return result.modified_count > 0

    def delete_game(self, game_id: str) -> bool:
        """從資料庫刪除遊戲記錄"""
        result = self.collection.delete_one({"_id": ObjectId(game_id)})
        return result.deleted_count > 0
