from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os

@app.route('/mkdir/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def mkdir(pwd, loc, name):
    if not check_pwd(pwd): return return_code(1)
    try:
        os.system("mkdir " + loc + "\\" + name)
        return return_code(0)
    except Exception as e:
        return return_code(999, str(e))


@app.route('/mkdir/<string:pwd>/<string:locname>', methods=['GET'])
def mkdir_whole(pwd, locname):
    if not check_pwd(pwd): return return_code(1)
    try:
        os.system("mkdir " + locname)
        return return_code(0)
    except Exception as e:
        return return_code(999, str(e))
