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
        self._player_name = player_name
        self.except_group_name = except_group_name

    @property
    def player_name(self):
        player_cursor = self.collection.find_one({"name": self._player_name})
        return player_cursor["name"]

    @player_name.setter
    def player_name(self,player_name):
        existing_player = self.collection.find_one({"name": player_name})
        if not existing_player:
            player_status = {"name": player_name}
            self.collection.insert_one(player_status)

    @property
    def group_names(self):
        cursor = self.collection.find({"name": self.player_name})
        return cursor[0]["group"]
    
    @group_names.setter
    def group_names(self,except_group_name):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"group": except_group_name}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    @property
    def player_seat(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["seat"]

    @player_seat.setter
    def player_seat(self, seat):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"seat": seat}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    @property
    def get_all_players_seat(self):
        all_player_seat = []
        for player in self.except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_seat = cursor["seat"]
            all_player_seat.append(player_seat)
        return all_player_seat
    
    @property
    def player_hp(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["HP"]

    @player_hp.setter
    def player_hp(self, hp):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"HP": hp}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    @property
    def get_all_players_hp(self):
        all_player_hp = []
        for player in self.except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_hp = cursor["HP"]
            all_player_hp.append(player_hp)
        return all_player_hp
    
    @property
    def player_score(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["score"]

    @player_score.setter
    def player_score(self, score):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"score": score}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    @property
    def get_all_players_score(self):
        all_player_score = []
        for player in self.except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_score = cursor["score"]
            all_player_score.append(player_score)
        return all_player_score
    
    @property
    def player_hand_stone(self):
        player_cursor = self.collection.find_one({"name": self.player_name})
        return player_cursor["hand_stone"]

    @player_hand_stone.setter
    def player_hand_stone(self, hand_stone):
        existing_player = self.collection.find_one({"name": self.player_name})
        if existing_player:
            player_status = {"hand_stone": hand_stone}
            self.collection.update_one(
                {"name": self.player_name}, {"$set": player_status}
            )

    @property
    def get_all_players_hand_stone(self):
        all_player_hand_stone = []
        for player in self.except_group_name:
            cursor = self.collection.find_one({"name": player})
            player_hand_stone = cursor["hand_stone"]
            all_player_hand_stone.append(player_hand_stone)
        return all_player_hand_stone

    def test(self, player_name, player_seat):
        existing_player = self.collection.find_one({"name": player_name})
        if existing_player:
            player_status = {"seat": player_seat}
            self.collection.update_one({"name": player_name}, {"$set": player_status})
