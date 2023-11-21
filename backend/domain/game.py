from random import shuffle
from dataclasses import dataclass
from .player import Player
from .spell import Spell
from .SPELLS import SPELLS


@dataclass
class Game:
    def __init__(self, game_id, players, active=True):
        self.game_id = game_id
        # 房間中的玩家
        self.players = [Player.from_dict(player) for player in players]

        self.active = active  # 遊戲是否進行中
        self.secret_warehouse = None  # 秘密魔法石放置處
        self.warehouse = None  # 未知牌堆放置位置
        self.ladder = None  # 放置成功施法的魔法
        self.round = None  # 達成加分條件時為一局
        self.turn = None  # 玩家從開始施法到結束稱為回合
        self.current_player = None  # 目前可進行施法動作玩家index
        self.spells = self.load_spells()  # 初始化所有可能的魔法石

    def load_spells(self):
        """載入遊戲中可能存在的魔法石"""
        return {
            "Magic 1": Spell("magic_1"),
            "Magic 2": Spell("magic_2"),
            "Magic 3": Spell("magic_3"),
            "Magic 4": Spell("magic_4"),
            "Magic 5": Spell("magic_5"),
            "Magic 6": Spell("magic_6"),
            "Magic 7": Spell("magic_7"),
            "Magic 8": Spell("magic_8"),
        }

    def cast_spell(self, player_id, spell_name):
        """施法，根據魔法石效果更新遊戲狀態"""
        player = self.find_player_by_id(player_id)
        spell = self.spells.get(spell_name)
        if spell:
            return spell.cast(self, player)
        return None

    def find_player_by_id(self, player_id):
        """取得與player_id相符合的Player class"""
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    def _shuffle_spells(self):
        all_spells = []
        for spell, count in SPELLS.items():
            all_spells.extend([spell] * count)
        shuffle(all_spells)
        return all_spells

    def init_game_state(self, game):
        all_spells = self._shuffle_spells()

        for player in game.players:
            player.initialize(all_spells[:5])
            # 每位玩家取得5個魔法石
            all_spells = all_spells[5:]

        game.current_player = 0

        game.secret_warehouse = all_spells[:4]
        game.warehouse = all_spells[4:]
        game.ladder = []
        return game

    def is_active(self):
        """檢查遊戲是否進行中"""
        return self.active

    def get_left_player(self, player):
        """取得玩家左側的Player class"""
        index = self.players.index(player)
        return self.players[(index + 1) % len(self.players)]

    def get_right_player(self, player):
        """取得玩家右側的Player class"""
        index = self.players.index(player)
        return self.players[(index - 1) % len(self.players)]

    def to_dict(self):
        data = {
            "game_id": self.game_id,
            "players": [player.to_dict() for player in self.players],
            "active": self.active,
        }

        if self.current_player is not None:
            data["current_player"] = self.current_player

        if self.round:
            data["round"] = self.round
        if self.turn:
            data["turn"] = self.turn

        if self.secret_warehouse:
            data["secret_warehouse"] = self.secret_warehouse
        else:
            data["secret_warehouse"] = None

        if self.warehouse:
            data["warehouse"] = self.warehouse
        else:
            data["warehouse"] = None

        if self.ladder:
            data["ladder"] = self.ladder
        else:
            data["ladder"] = None

        return data

    @classmethod
    def from_dict(cls, data):
        game = cls(
            game_id=data["game_id"],
            players=data["players"],
            active=data.get("active", True),
        )

        if "current_player" in data:
            game.current_player = data["current_player"]

        if "round" in data:
            game.round = data["round"]
        if "turn" in data:
            game.turn = data["turn"]

        if "secret_warehouse" in data:
            game.secret_warehouse = data["secret_warehouse"]
        if "warehouse" in data:
            game.warehouse = data["warehouse"]
        if "ladder" in data:
            game.ladder = data["ladder"]

        game.spells = game.load_spells()
        return game
