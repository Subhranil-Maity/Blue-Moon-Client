from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os

@app.route('/delete/<string:pwd>/<string:path>', methods=['GET'])
def delete(pwd, path: str):
    if not check_pwd(pwd): return return_code(1)
    try:
        if os.path.isdir(path):
            os.system("rmdir /q /s " + path)
        elif os.path.isfile(path):
            os.system("del /f " + path)
        else:
            return return_code(2)
        return return_code(0)
    except Exception as e:
        return return_code(999, str(e))