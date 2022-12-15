from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os

@app.route('/delete/<string:pwd>/<string:path>', methods=['GET'])
def delete(pwd, path: str):
    if not check_pwd(pwd): return returnCode(1)
    try:
        if os.path.isdir(path):
            os.system("rmdir /q /s " + path)
        elif os.path.isfile(path):
            os.system("del /f " + path)
        else:
            return returnCode(2)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))