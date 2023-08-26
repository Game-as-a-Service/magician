from flask import Flask, request
from flask_cors import CORS
from magician.service.print_hello import print_hello
from magician.service.game_create import game_create
from magician.service.spelling import spelling

app = Flask(__name__)
CORS(app)


@app.route("/hello", methods=["GET"])
def api_hello():
    return {"msg": print_hello()}, 200


@app.route("/gameCreate", methods=["POST"])
def api_GameCreate():
    player = request.get_json()
    result = game_create(player)

    match result:
        case "start game":
            return {"msg": result}, 201
        case "players is not enough" | "players is over 5":
            return {"msg": result}, 400
        case _:
            return {"msg": "Unknow error"}, 500


@app.route("/player/<playerID>/join", methods=["PUT"])
def api_game_join(playerID):
    # print("Player ID is %s" % playerID)
    return {"msg": playerID}, 200


@app.route("/stone", methods=["PATCH"])
def api_spelling():
    spell = request.get_json()
    result = spelling(spell)

    match result:
        case "magic exist":
            return {"msg": spell["stoneID"]}, 200
        case "magic doesn't exist":
            return {"msg": result}, 400
        case _:
            return {"msg": "Unknow error"}, 501
