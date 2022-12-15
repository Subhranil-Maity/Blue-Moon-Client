from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os

@app.route('/type/<string:pwd>/<string:path>', methods=['GET'])
def get_content(pwd, path):
    if not check_pwd(pwd): return returnCode(1)
    try:
        with open(path, 'r') as handle:
            data = handle.read()
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))