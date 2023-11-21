import random


def roll_dice():
    """模擬擲骰子的動作，回傳一個隨機數字，介於1~3之間"""
    return random.randint(1, 3)


class Spell:
    def __init__(self, name):
        self.name = name  # 魔法石名稱

    def __get_method_name(self):
        return f'cast_{self.name.replace(" ", "_").lower()}'

    def get_value(self):
        """取得施法編號"""
        return int(self.name.split(" ")[1])

    def valid_spell_name(self):
        """驗證魔法石名稱是否有效"""
        if self.name == "unknown":
            return False

        method_name = self.__get_method_name()

        if hasattr(Spell, method_name):
            return True
        else:
            return False

    def cast(self, game, player):
        """
        通用施法函數

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        # 根據魔法石名稱呼叫相對應的方法
        method_name = self.__get_method_name()
        cast_method = getattr(self, method_name, self.cast_unknown)
        return cast_method(game, player)

    def cast_unknown(self, game, player):
        """
        保留(當魔法石名稱無效時)

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        print(f"{player.name} tries to cast an unknown spell: {self.name}!")
        return "unknown spell", None

    def cast_magic_1(self, game, player):
        """
        火龍
        其他所有玩家扣除擲一次骰子點數的血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """

        for p in game.players:
            if p != player:
                damage = roll_dice()
                p.update_HP(-damage)
        return "fire_dragon", damage

    def cast_magic_2(self, game, player):
        """
        暗黑幽靈
        其他所有玩家失去1點血量,自己回復1點血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        for p in game.players:
            if p != player:
                p.update_HP(-1)
        player.update_HP(1)
        return "dark_ghost", 1

    def cast_magic_3(self, game, player):
        """
        甜蜜的夢
        回復擲一次骰子點數的血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        healing = roll_dice()
        player.update_HP(healing)
        return "sweet_dream", healing

    def cast_magic_4(self, game, player):
        """
        貓頭鷹
        從祕密倉庫取得一張魔法石，並且放入玩家的祕密魔法石列表

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """

        # 檢查祕密倉庫是否還有魔法石
        if len(game.secret_warehouse) > 0:
            # 從祕密倉庫取得一張魔法石
            secret_spell = game.secret_warehouse.pop()

            # 放入玩家的祕密魔法石列表
            player.secret_spells.append(secret_spell)

        else:
            # 祕密倉庫沒有魔法石
            secret_spell = None

        return "owl", secret_spell

    def cast_magic_5(self, game, player):
        """
        閃電暴風雨
        左右手邊玩家失去1點血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        left_player = game.get_left_player(player)
        left_player.update_HP(-1)

        right_player = game.get_right_player(player)
        right_player.update_HP(-1)
        return "lightning_storm", 1

    def cast_magic_6(self, game, player):
        """
        暴風雪
        左手邊玩家失去1點血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        left_player = game.get_left_player(player)
        left_player.update_HP(-1)
        return "blizzard", 1

    def cast_magic_7(self, game, player):
        """
        火球
        右手邊玩家失去1點血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        right_player = game.get_right_player(player)
        right_player.update_HP(-1)
        return "fireball", 1

    def cast_magic_8(self, game, player):
        """
        魔法藥水
        回復1點血量

        :param game: 目前遊戲狀態，從資料庫取出
        :param player: 施法玩家
        """
        player.update_HP(1)
        return "magic_potion", 1
