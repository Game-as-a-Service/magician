import pymongo


class Player_repository:
    def __init__(
        self,
        player_name=None,
        except_group_name=None,
    ):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.player_status
        self.player_name = player_name
        self.except_group_name = except_group_name

    def set_player_name(self):
        existing_player = self.collection.find_one({"name": self.player_name})
        if not existing_player:
            player_status = {"name": self.player_name, "group": self.except_group_name}
            self.collection.insert_one(player_status)

    def get_player_name(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["name"]

    def get_group_names(self):
        cursor = self.collection.find({"name": self.player_name})
        return cursor[0]["group"]

    def set_player_seat(self, seat):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"seat": seat}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    def get_player_seat(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["seat"]

    def get_all_players_seat(self, except_group_name):
        all_player_seat = []
        for player in except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_seat = cursor["seat"]
            all_player_seat.append(player_seat)
        return all_player_seat

    def set_player_hp(self, hp):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"HP": hp}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    def get_player_hp(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["HP"]

    def get_all_players_hp(self, except_input_name):
        all_player_hp = []
        for player in except_input_name:
            cursor = self.collection.find_one({"name": player})
            player_hp = cursor["HP"]
            all_player_hp.append(player_hp)
        return all_player_hp

    def set_player_score(self, score):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"score": score}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    def get_player_score(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["score"]

    def get_all_players_score(self, except_input_name):
        all_player_score = []
        for player in except_input_name:
            cursor = self.collection.find_one({"name": player})
            player_score = cursor["score"]
            all_player_score.append(player_score)
        return all_player_score

    def set_player_hand_stone(self, hand_stone):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"hand_stone": hand_stone}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    def get_player_hand_stone(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["hand_stone"]

    def get_all_players_hand_stone(self, except_group_name):
        all_player_hand_stone = []
        for player in except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_hand_stone = cursor["hand_stone"]
            all_player_hand_stone.append(player_hand_stone)
        return all_player_hand_stone

    def test(self, player_name, player_seat):
        existing_player = self.collection.find_one({"name": player_name})
        if existing_player:
            player_status = {"seat": player_seat}
            self.collection.update_one({"name": player_name}, {"$set": player_status})
