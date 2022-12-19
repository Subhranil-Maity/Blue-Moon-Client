from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request
import os


@app.route('/delete/', methods=['DELETE'])
def delete():
    pwd = request.args.get('pwd')
    path = request.args.get('path')
    if not check_pwd(pwd): return "error: invalid pwd"
    try:
        if os.path.isdir(path):
            os.system("rmdir /q /s " + path)
        elif os.path.isfile(path):
            os.system("del /f " + path)
        else:
            return {}
        return {}
    except Exception as e:
        return str(e)
