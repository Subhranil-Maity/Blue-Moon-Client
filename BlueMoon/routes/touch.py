from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request
import os


@app.route('/touch/', methods=['POST'])
def touch():
    try:
        pwd = request.args.get('pwd')
        loc = request.args.get('loc')
        name = request.args.get('name')
        if not check_pwd(pwd): return return_code(1)
        os.system("type nul >>" + loc + "\\" + name)
        return {}
    except Exception as e:
        return str(e)
