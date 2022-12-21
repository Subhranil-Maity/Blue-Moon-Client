from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request, send_file
import os

from BlueMoon.utils.get import get_path_params


@app.route('/getfile', methods=['GET'])
def get_file_route():
    check_password(request.args)
    try:
        return get_file(
            path=get_path_params(request.args)
        )
    except Exception as e:
        return str(e)
