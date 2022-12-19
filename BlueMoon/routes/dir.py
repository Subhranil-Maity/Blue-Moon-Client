from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os


@app.route('/dir/<string:pwd>/<string:loc>', methods=['GET'])
def get_dir(pwd: str, loc):
    try:
        if not check_pwd(pwd): return return_code(1, extras="content", data=[])
        if not os.path.isdir(loc): return return_code(2, extras="content", data=[])
        return returnDir(loc)
    except Exception as e:
        return return_code(e)
