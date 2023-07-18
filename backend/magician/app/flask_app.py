from flask import Flask
from flask_cors import CORS
from magician.service.print_hello import print_hello

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def api_hello():
    return {"msg": print_hello()}, 200
