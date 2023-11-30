import os
import socketio
from flask import Flask

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = os.environ.get("REDIS_PORT") or 6379
REDIS_DB = os.environ.get("REDIS_DB") or 0
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or None
REDIS_PROTOCOL = os.environ.get("REDIS_PROTOCOL") or "redis"

if REDIS_PASSWORD:
    REDIS_URI = f"{REDIS_PROTOCOL}://default:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
else:
    REDIS_URI = f"{REDIS_PROTOCOL}://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

mgr = socketio.RedisManager(REDIS_URI)
sio = socketio.Server(client_manager=mgr, cors_allowed_origins="*")
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)


@sio.event
def connect(sid, environ):
    print("connect ", sid)


active_players = {}


@sio.on("player_joined")
def player_joined(sid, data):
    player_id = data.get("player_id")
    active_players[sid] = {"player_id": player_id}
    sio.enter_room(sid, player_id)
    sio.emit("player_joined", {"player_id": player_id}, room=player_id)
    print(active_players)


if __name__ == "__main__":
    socketio.run(app, debug=True)
