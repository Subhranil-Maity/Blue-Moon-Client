from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os

@app.route('/mkdir/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def mkdir(pwd, loc, name):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("mkdir " + loc + "\\" + name)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))


@app.route('/mkdir/<string:pwd>/<string:locname>', methods=['GET'])
def mkdir_whole(pwd, locname):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("mkdir " + locname)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))
