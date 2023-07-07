from flask import Flask

from magician.service.print_hello import print_hello

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def api_hello():
    return {"msg": print_hello()}, 200
