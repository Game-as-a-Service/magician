import pymongo

class Player_repository:
    def __init__(self, players=None, except_input_name=None,except_input_seat=None,except_input_hp=None,except_input_score=None): #資料內容名稱可以重改
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.magician
        self.collection = self.db.player_status
        self.players = players
        self.except_input_name = except_input_name
        self.except_input_seat = except_input_seat
        self.except_input_hp = except_input_hp
        self.except_input_score = except_input_score
            
    def set_player_name(self):
        existing_player = self.collection.find_one({"name": self.players})
        if not existing_player:
            player_status = {"name": self.players, "group": self.except_input_name}
            self.collection.insert_one(player_status)

    def get_player_names(self):        
        cursor = self.collection.find({"name": self.players})
        return cursor[0]["group"]
    

    def set_players_seat(self,seat):
        existing_player = self.collection.find_one({"name": self.players})
        if existing_player:
            player_status = {"seat": seat}
            self.collection.update_one({"name": self.players}, {"$set": player_status})
        
    def get_players_seat(self,except_input_name):
        all_player_seat = []
        for player in except_input_name:
            cursor = self.collection.find_one({"name": player})
            player_seat = cursor["seat"]
            all_player_seat.append(player_seat)
        return all_player_seat


    def set_players_hp(self,hp):
        existing_player = self.collection.find_one({"name": self.players})
        if existing_player:
            player_status = {"HP": hp}
            self.collection.update_one({"name": self.players}, {"$set": player_status})
    
    def get_players_hp(self,except_input_name):
        all_player_hp = []
        for player in except_input_name:
            cursor = self.collection.find_one({"name":player})
            player_hp = cursor["HP"]
            all_player_hp.append(player_hp)
        return all_player_hp

    def set_players_score(self,score):
        existing_player = self.collection.find_one({"name": self.players})
        if existing_player:
            player_status = {"score": score}
            self.collection.update_one({"name": self.players}, {"$set": player_status})
    
    def get_players_score(self,except_input_name):
        all_player_score = []
        for player in except_input_name:
            cursor = self.collection.find_one({"name":player})
            player_score = cursor["score"]
            all_player_score.append(player_score)
        return all_player_score

    def gather_status(self):
        cursor = self.collection.find({"name": self.except_input_name})
        self.except_input_seat = cursor[0]["seat"]
        self.except_input_HP = cursor[0]["HP"]
        self.except_input_score = cursor[0]["score"]        


    def set_player_hand_stone(self, hand_stone): #set_hand_stone
        existing_player = self.collection.find_one({"name": self.players})
        if existing_player:
            player_status = {"hand_stone": hand_stone}
            self.collection.update_one({"name": self.players}, {"$set": player_status})
        #    return existing_player["name"]
        #else:
        #    return -1
    
    def get_hand_stone(self):
        existing_hand_stone = self.collection.find_one({"name": self.players})
        return existing_hand_stone["hand_stone"]

    def test(self, player_name, player_seat):
        existing_player = self.collection.find_one({"name": player_name})
        if existing_player:
            player_status = {"seat": player_seat}
            self.collection.update_one({"name": player_name}, {"$set": player_status})


