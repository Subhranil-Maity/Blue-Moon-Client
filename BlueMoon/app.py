from flask import Flask
import sys
from BlueMoon.utils.storage import Config, load_config
app = Flask(__name__)
config: Config = load_config()
from BlueMoon.routes import *





def start_server():
    if len(sys.argv) >= 3:
        app.run(debug=True if "-d" in sys.argv else False, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True if "-d" in sys.argv else False, host='0.0.0.0', port=65432)


if __name__ == '__main__':
    start_server()
