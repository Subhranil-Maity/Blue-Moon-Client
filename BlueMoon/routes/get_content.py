from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request, send_file
import os


@app.route('/getfile/', methods=['GET'])
def get_file():
    try:
        pwd = request.args.get('pwd')
        path = request.args.get('path')
        if not check_pwd(pwd): return return_code(1)
        name = path.split('\\')
        return send_file(open(path, 'rb'), mimetype=None, download_name=name[len(name) - 1])
    except Exception as e:
        return str(e)
