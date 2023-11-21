from repository.player_repository import PlayerRepository
from domain.player import Player


class PlayerService:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def create_player(self, name):
        """建立玩家class並存到資料庫內"""
        new_player = Player(player_id=None, name=name)
        player_id = self.player_repository.create_player(new_player)
        return player_id

    def get_player(self, player_id):
        """從資料庫內取得玩家資訊"""
        return self.player_repository.get_player_by_id(player_id)
