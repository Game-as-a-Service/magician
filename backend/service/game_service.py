from typing import Tuple
from bson.objectid import ObjectId
from repository.game_repository import GameRepository
from domain.game import Game
from domain.spell import Spell, roll_dice


class GameService:
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository

    def create_game(self, player_ids: list[str]) -> Game:
        game = Game(game_id=None, players=player_ids)
        game_id = self.game_repository.create_game(game)
        game.game_id = game_id  # 從資料取得的game_id
        game.action_message = "開始遊戲"
        self.game_repository.update_game(game)
        return game

    def player_join_game(self, game_id: str, player_id: str) -> bool:
        game = self.game_repository.get_game_by_id(game_id)
        if not (game and game.is_active()):
            # 從資料庫確認game_id存在，並且遊戲進行中
            return False
        player_joined_stat = False
        if game:
            player = next((p for p in game.players if p.player_id == player_id), None)
            if player:
                if player.joined:
                    return False
                player.joined = True
                game.action_message = player.player_id + " 加入遊戲"
                self.game_repository.update_game(game)
                player_joined_stat = True

        all_joined = all(p.joined for p in game.players)

        if all_joined:
            game = self.start_game(game)
            game.action_message = "回合開始"
            self.game_repository.update_game(game)
            
        return player_joined_stat

    def start_game(self, game: Game) -> Game:
        game = game.init_game_state(game)

        game.round = 1
        game.turn = 1

        return game

    def cast_spell(
        self, game_id: str, player_id: str, spell_name: str
    ) -> Tuple[bool, int]:
        """玩家施法邏輯"""
        game = self.game_repository.get_game_by_id(game_id)
        if not (game and game.is_active()):
            # 從資料庫確認game_id存在，並且遊戲進行中
            return False, 400
        if game.current_player is None:
            return False, 400
        # player_id為目前正在行動玩家
        current_player_id = game.players[game.current_player].player_id
        if player_id != current_player_id:
            return False, 400

        # 確認法術存在
        player = game.find_player_by_id(player_id)
        spell = Spell(spell_name)
        if not spell.valid_spell_name():
            return False, 400

        if player.prev_spell:
            spell_prve = Spell(player.prev_spell)
            if spell.get_value() < spell_prve.get_value():
                return False, 400

        player.prev_spell = spell_name
        if spell_name not in player.spells:
            # 施法失敗
            hp_damge = -1
            if spell_name == "Magic 1":
                # 喊得是火龍，玩家擲骰扣HP
                hp_damge = roll_dice() * -1                
            player.update_HP(hp_damge)
            game.action_message = player.player_id + " 施放 " +spell_name + " 失敗自損 " + str(abs(hp_damge)) +" 滴血"
            self.game_repository.update_game(game)

            if player.get_HP() == 0:
                # 當玩家把自己血量歸0
                # 結束這一局，結算分數
                self.end_round(game_id, player_id)
            # 本回合結束
            self.end_turn(game_id, player_id)

            return False, 200

        # 施法成功

        # 玩家手牌移除對應魔法石
        player.spells.remove(spell_name)

        # 玩家把手上所有的魔法石都用完了
        if len(player.spells) == 0:
            # 儲存目前遊戲狀態
            game.action_message = player.player_id + " 手牌魔法石出完，局結束，結算分數"
            self.game_repository.update_game(game)
            # 結束這一局，結算分數
            self.end_round(game_id, player_id)
            # 不執行施放魔法石效果
            # 避免觸發造成其他玩家血量歸0條件
            # 這樣會造成重複加分超過3分
            return True, 200

        # 執行魔法石效果
        spell.cast(game, player)

        if game.ladder is None:
            game.ladder = []
        # 將手牌放置於階梯
        game.ladder.append(spell_name)
        # 儲存目前遊戲狀態
        game.action_message = player.player_id + " 施法 " + spell_name +" 成功 "
        self.game_repository.update_game(game)

        for p in game.players:
            if p.get_HP() == 0:
                # 有玩家的血量歸0
                # 結束這一局，結算分數
                self.end_round(game_id, game.players[game.current_player].player_id)

        return True, 200

    def end_turn(self, game_id: str, player_id: str) -> bool:
        """結束目前回合，並且保存遊戲狀態至資料庫"""
        game = self.game_repository.get_game_by_id(game_id)

        if not (game and game.is_active()):
            # 從資料庫確認game_id存在，並且遊戲進行中
            return False

        if game.current_player is None:
            return False

        current_player_id = game.players[game.current_player].player_id
        if player_id != current_player_id:
            return False

        player = game.find_player_by_id(player_id)

        if player.prev_spell:
            player.prev_spell = None  # 清空施法紀錄
        else:
            return False  # 至少需要施法過一次

        # 換下一位玩家
        game.current_player += 1
        if game.current_player >= len(game.players):
            game.current_player = 0
        game.turn += 1

        # 回合結束，檢查玩家魔法石數量
        if len(player.spells) < 5:
            # 計算需要補充的魔法石數量
            refill_count = 5 - len(player.spells)

            # 從倉庫補充魔法石
            for i in range(refill_count):
                if game.warehouse:
                    be_hand_stone = game.warehouse.pop()
                    player.spells.append(be_hand_stone)
        game.action_message = player.player_id + " 回合結束"
        self.game_repository.update_game(game)

        return True

    def end_round(self, game_id: str, player_id: str) -> None:
        # 局結束
        game = self.game_repository.get_game_by_id(game_id)
        player = game.find_player_by_id(player_id)

        if len(player.spells) == 0:
            # 局結束條件：玩家將魔法石都用完了
            player.update_score(3)
        else:
            # 局結束條件：某玩家血量歸0
            for p in game.players:
                if p.get_HP() > 0:
                    # 存活者加1分
                    p.update_score(1)

                    if p.player_id == player_id:
                        # 勝利者總共加分3分
                        p.update_score(2)

        for p in game.players:
            if p.get_HP() > 0:
                if len(p.secret_spells) > 0:
                    # 持有秘密魔法石，有幾個加幾分
                    p.update_score(len(p.secret_spells))
        game.action_message = "新局開始"
        self.game_repository.update_game(game)
        self.start_new_round(game_id)

    def start_new_round(self, game_id: str) -> None:
        game = self.game_repository.get_game_by_id(game_id)

        game = game.init_game_state(game)

        game.round += 1
        game.turn = 1

        game.shuffle_player()
        game.action_message = "回合開始"
        self.game_repository.update_game(game)

        for player in game.players:
            if player.score >= 8:
                # 已有玩家獲得8分
                # 遊戲結束
                game.active = False
                game.action_message = "有玩家獲得8分，遊戲結束"
                self.game_repository.update_game(game)

    def player_status(self, game_id: str, player_id: str):
        # TODO
        # 與backend\repository\redis_repository.py內的
        # publish隱函數convert_object_id重複
        # 可合併為utility function
        def convert_object_id(data):
            if isinstance(data, dict):
                for k, v in data.items():
                    data[k] = convert_object_id(v)
            elif isinstance(data, ObjectId):
                return str(data)
            return data

        game = self.game_repository.get_game_by_id(game_id)
        if game:  
            # [待討論]新增一個玩家是否存在的判斷?
            query_result = game.real_game_can_see(player_id).to_dict()
            return convert_object_id(query_result)
        return None
