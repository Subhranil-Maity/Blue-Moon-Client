from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os

@app.route('/touch/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def touch(pwd, loc, name):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("type nul >>" + loc + "\\" + name)
        return returnCode(0)
    except Exception as e:
        returnCode(999, str(e))


@app.route('/touch/<string:pwd>/<string:locname>', methods=['GET'])
def touch_whole(pwd, locname):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("type nul >>" + locname)
        return returnCode(0)
    except Exception as e:
        returnCode(999, str(e))

