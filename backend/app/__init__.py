import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from .services import GameService
from .config import DevelopmentConfig, ProductionConfig
from functools import wraps
import jwt
from jwt import PyJWKClient
import requests

app = Flask(__name__)
CORS(app)

if app.config is None:
    if os.environ.get("MONGO_DB_NAME") is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"message": "Invalid token format"}), 401

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            url = "https://dev-1l0ixjw8yohsluoi.us.auth0.com/.well-known/jwks.json"
            jwks_client = PyJWKClient(url)
            signing_key = jwks_client.get_signing_key_from_jwt(token)
            jwt.decode(
                token,
                signing_key,
                audience="https://api.gaas.waterballsa.tw",
                options={"verify_exp": True},
                algorithms=["RS256"],
            )

            # Fetch user details from GaaS API
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                "https://api.gaas.waterballsa.tw/users/me", headers=headers
            )
            if response.status_code != 200:
                return jsonify({"message": "Failed to fetch user details"}), 401

            user_data = response.json()
            current_user = user_data["id"]
            nickname = user_data["nickname"]

        except Exception as e:
            return jsonify({"message": f"Invalid token: {e}"}), 401

        return f(current_user, nickname, *args, **kwargs)

    return decorated


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

    result = GameService.player_join_game(room_id, player_id)
    if result["success"]:
        return (
            jsonify({"message": "Player joined the game", "gameRoomID": room_id}),
            200,
        )
    else:
        return jsonify({"error": result["message"]}), result["status_code"]


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
    result = GameService.spell_stop(gameRoomID, player_id)
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


@app.route("/endgame", methods=["DELETE"])
@jwt_required
def end_game(current_user, nickname):
    data = request.json
    gameRoomID = data.get("gameRoomID")
    if not gameRoomID:
        return jsonify({"message": "gameRoomID is required"}), 400

    token = None
    if "Authorization" in request.headers:
        auth_header = request.headers["Authorization"]
        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({"message": "Invalid token format"}), 401

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"https://api.gaas.waterballsa.tw/rooms/{gameRoomID}:endGame",
        headers=headers,
    )
    if response.status_code != 204:
        return (
            jsonify(
                {
                    "message": f"Failed to end game on GaaS platform: {response.status_code}",
                }
            ),
            400,
        )
    else:
        return jsonify({"message": "Game ended successfully"}), 204


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


@app.route("/games", methods=["POST"])
@jwt_required
def start_game(current_user, nickname):
    data = request.json
    room_id = data.get("roomId")
    players = data.get("players")

    if not room_id or not players:
        return jsonify({"message": "Room ID and players are required"}), 400

    if len(players) != 5:
        return jsonify({"message": "Number of players must be 5"}), 400

    player_ids = [player["id"] for player in players]
    player_nickname = [player["nickname"] for player in players]

    if current_user not in player_ids:
        return jsonify({"message": "Unauthorized to start this game"}), 403

    room_id = GameService.create_game(player_ids, player_nickname)
    gameRoomID = str(room_id.game_id)
    return (
        jsonify(
            {
                "message": "Game created",
                "gameRoomID": gameRoomID,
                "url": f"https://game-as-a-service.github.io/magician/#/{gameRoomID}/",
            }
        ),
        201,
    )


@app.route("/me", methods=["GET"])
@jwt_required
def get_user_info(current_user, nickname):
    return jsonify({"player_id": current_user, "player_nickname": nickname}), 200
