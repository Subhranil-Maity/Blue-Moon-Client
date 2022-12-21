from flask import request

from BlueMoon.app import app
from BlueMoon.utils.auth import check_password
from BlueMoon.utils.get import get_path_params
from BlueMoon.utils.functions import *
from BlueMoon.utils.errors import *
import os


@app.route('/dir', methods=['GET'])
def get_dir_route():
    check_password(request.args)
    try:
        return get_dir(
            get_path_params(request.args)
        )
    except Exception as e:
        return error(e)
