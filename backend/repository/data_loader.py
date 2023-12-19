from .redis_repository import RedisRepository


class DataLoader:
    def __init__(
        self,
        emitter=None,
        repo=None,
    ):
        if emitter:
            self.emitter = emitter
        else:
            self.emitter = None
        if repo:
            self.repo = repo
        else:
            self.repo = None
        self.redis_repo = RedisRepository()
        if self.emitter:
            self.emitter.on("game_updated", self.handle_game_updated)

    def handle_game_updated(self, game_id: str) -> None:
        game = self.repo.get_game_by_id(game_id)
        for player in game.players:
            real_game = game.real_game_can_see(player.player_id)
            self.redis_repo.publish(
                "game_update", str(player.player_id), real_game.to_dict()
            )
