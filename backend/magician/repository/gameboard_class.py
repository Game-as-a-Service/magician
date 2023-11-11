import pymongo

class gameboard_repository:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.gameboard
        self._group = []

    @property
    def group_names(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["group"]

    @group_names.setter
    def group_names(self,except_group_name):
        existing_group = self.collection.find_one({"group": except_group_name})
        if not existing_group:
            gameboard = {"group": except_group_name}
            self.collection.insert_one(gameboard)
        self._group = except_group_name

    @property
    def secret_stone(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["secret_stone"]

    @secret_stone.setter
    def secret_stone(self,except_secret_stone):
        existing_group = self.collection.find_one({"group": self._group})
        if existing_group:
            gameboard = {"secret_stone": except_secret_stone}
            self.collection.update_one(
                {"group": self._group}, {"$set": gameboard}
            )

    @property
    def unknown_stone(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["unknown_stone"]

    @unknown_stone.setter
    def unknown_stone(self,except_unknown_stone):
        existing_group = self.collection.find_one({"group": self._group})
        if existing_group:
            gameboard = {"unknown_stone": except_unknown_stone}
            self.collection.update_one(
                {"group": self._group}, {"$set": gameboard}
            )

    @property
    def ladder(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["ladder"]

    @ladder.setter
    def ladder(self,except_ladder):
        existing_group = self.collection.find_one({"group": self._group})
        if existing_group:
            gameboard = {"ladder": except_ladder}
            self.collection.update_one(
                {"group": self._group}, {"$set": gameboard}
            )
    
    @property
    def round(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["round"]

    @round.setter
    def round(self,except_round):
        existing_group = self.collection.find_one({"group": self._group})
        if existing_group:
            gameboard = {"round": except_round}
            self.collection.update_one(
                {"group": self._group}, {"$set": gameboard}
            )

    @property
    def turn(self):
        gameboard_cursor = self.collection.find_one({"group": self._group})
        return gameboard_cursor["turn"]

    @turn.setter
    def turn(self,except_turn):
        existing_group = self.collection.find_one({"group": self._group})
        if existing_group:
            gameboard = {"turn": except_turn}
            self.collection.update_one(
                {"group": self._group}, {"$set": gameboard}
            )