from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os

@app.route('/touch/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def touch(pwd, loc, name):
    if not check_pwd(pwd): return return_code(1)
    try:
        os.system("type nul >>" + loc + "\\" + name)
        return return_code(0)
    except Exception as e:
        return_code(999, str(e))


@app.route('/touch/<string:pwd>/<string:locname>', methods=['GET'])
def touch_whole(pwd, locname):
    if not check_pwd(pwd): return return_code(1)
    try:
        os.system("type nul >>" + locname)
        return return_code(0)
    except Exception as e:
        return_code(999, str(e))

