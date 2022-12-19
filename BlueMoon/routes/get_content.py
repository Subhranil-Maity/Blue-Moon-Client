from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os

@app.route('/type/<string:pwd>/<string:path>', methods=['GET'])
def get_content(pwd, path):
    if not check_pwd(pwd): return return_code(1)
    try:
        with open(path, 'r') as handle:
            data = handle.read()
        return return_code(0)
    except Exception as e:
        return return_code(999, str(e))