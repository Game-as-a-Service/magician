import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from .services import GameService
from .config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
CORS(app)

if app.config is None:
    if os.environ.get("MONGO_DB_NAME") is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)


@app.route("/gameCreate", methods=["POST"])
def create_game():
    data = request.json
    player_ids = data.get("playerIDs")
    if not player_ids:
        return jsonify({"message": "Player IDs are required"}), 400

    if len(player_ids) <= 3:
        return jsonify({"message": "Number of players must be greater than 3"}), 400

    if len(player_ids) > 5:
        return jsonify({"message": "Number of players cannot exceed 5"}), 400

    room_id = GameService.create_game(player_ids)
    print("room_id: ", room_id.game_id)
    return jsonify({"message": "Game created", "gameRoomID": str(room_id.game_id)}), 201


@app.route("/player/<player_id>/join", methods=["PUT"])
def player_join_game(player_id):
    if not player_id:
        return jsonify({"error": "Player ID required"}), 404
    data = request.json
    room_id = data.get("gameRoomID")
    if not room_id:
        return jsonify({"error": "Game room ID required"}), 400

    if GameService.player_join_game(room_id, player_id):
        return (
            jsonify({"message": "Player joined the game", "gameRoomID": room_id}),
            200,
        )
    else:
        return jsonify({"message": "Unable to join game"}), 400


@app.route("/stone", methods=["PATCH"])
def cast_spell():
    data = request.json
    gameRoomID = data.get("gameRoomID")
    player_id = data.get("playerID")
    spell_name = data.get("spellName")

    if not gameRoomID:
        return jsonify({"message": "gameRoomID is required"}), 400

    if not player_id or not spell_name:
        return jsonify({"message": "Player ID and spell name are required"}), 400

    result, status_code = GameService.cast_spell(gameRoomID, player_id, spell_name)
    if result:
        return jsonify({"message": "Spell cast successfully"}), status_code
    else:
        return jsonify({"message": "Spell cast failed"}), status_code


@app.route("/player/<player_id>/spellstop", methods=["PATCH"])
def stop_spell(player_id):
    if not player_id:
        return jsonify({"message": "Player ID is required"}), 400
    data = request.json
    gameRoomID = data.get("gameRoomID")
    result = GameService.end_turn(gameRoomID, player_id)
    if result:
        return jsonify({"message": "Player turn ended"}), 200
    else:
        return jsonify({"message": "Player turn failed"}), 400


@app.route("/player/status", methods=["GET"])
def player_status():
    player_id = request.args.get("player_id")
    gameRoomID = request.args.get("gameRoomID")
    if not player_id:
        return jsonify({"message": "player_id not found"}), 400
    if not gameRoomID:
        return jsonify({"message": "gameRoomID not found"}), 400

    result = GameService.player_status(gameRoomID, player_id)
    if result:
        return result, 200
    else:
        return jsonify({"message": "gameRoomID does not exist"}), 400
