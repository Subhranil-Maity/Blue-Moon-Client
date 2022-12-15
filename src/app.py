
import sys

from flask import *
app = Flask(__name__)
from src.routes import *


def start_server():
    if len(sys.argv) >= 3:
        app.run(debug=True if "-d" in sys.argv else False, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True if "-d" in sys.argv else False, host='0.0.0.0', port=5555)


if __name__ == '__main__':
    start_server()