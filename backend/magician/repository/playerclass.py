import pymongo


class Player:
    def __init__(self, player_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.player_status
        self.player_name = player_name
        self.update_player_status(self.player_name)

    def update_player_status(self, player_name):
        existing_player = self.collection.find_one({"name": player_name})
        if not existing_player:
            player_status = {"name": player_name}
            self.collection.insert_one(player_status)
        self.get_all_player_names()

    def get_all_player_names(self):
        self.player_name
        all_player_names = []
        cursor = self.collection.find({})
        for player_doc in cursor:
            player_name = player_doc["name"]
            all_player_names.append(player_name)
        return all_player_names

    # class PlayerSeat:

    # self.client = pymongo.MongoClient("mongodb://localhost:27017")
    # self.db = self.client.magician
    # self.collection = self.db.player_status
    # #self.player_name = player_name
    # self.player_name = player_seat
    def test(self, player_name, player_seat):
        existing_player = self.collection.find_one({"name": player_name})
        if existing_player:
            player_status = {"seat": player_seat}
            self.collection.update_one({"name": player_name}, {"$set": player_status})


# def player_status(players_name):
#    client = pymongo.MongoClient("mongodb://localhost:27017")
#    db = client.magician
#    collection = db.player_status
#
#
#    class playername:
#        def name(self):
#            existing_player = collection.find_one({"name": players_name})
#            if not existing_player:
#
#                player_status = {
#                    "name": players_name
#                }
#                collection.update_one({"name": players_name}, {"$set": player_status})
#
#            all_player_names = []
#            cursor = collection.find({})
#            for player_doc in cursor:
#                player_name = player_doc["name"]
#                all_player_names.append(player_name)
#
#            return all_player_names
#
#    class seat:
#        pass
