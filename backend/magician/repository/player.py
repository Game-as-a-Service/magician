import pymongo


def player_status(players_name):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.magician
    collection = db.player_status

    # 创建唯一索引，确保 'name' 字段的值是唯一的
    # collection.create_index([('name', pymongo.ASCENDING)], unique=True)

    # 查询数据库，检查是否已存在相同 'name' 字段的记录
    existing_player = collection.find_one({"name": players_name})

    if existing_player:
        # 如果已存在相同 'name' 的记录，直接返回已存在的数据
        # return existing_player
        # player_status = {
        #     "name": players_name,
        #     "HP": "6",
        #     "score": "0",
        #     "seat": 1,
        # }
        # collection.update_one({"name": players_name}, {"$set": player_status})
        pass
    else:
        player_status = {
            "name": players_name,
            "HP": "6",
            "score": "0",
            "seat": None,
        }
        collection.insert_one(player_status)

    # return player_status['name']

    all_player_names = []
    cursor = collection.find({})
    for player_doc in cursor:
        player_name = player_doc["name"]
        all_player_names.append(player_name)

    # 現在 all_player_names 列表中包含了所有玩家的名稱
    # print(all_player_names)
    return all_player_names
