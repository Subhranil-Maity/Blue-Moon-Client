from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os


@app.route('/dir/<string:pwd>/<string:loc>', methods=['GET'])
def get_dir(pwd: str, loc):
    try:
        if not check_pwd(pwd): return returnCode(1, extras="content", data=[])
        if not os.path.isdir(loc): return returnCode(2, extras="content", data=[])
        return returnDir(loc)
    except Exception as e:
        return returnCode(e)
