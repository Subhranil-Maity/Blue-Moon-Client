from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request
import os

from BlueMoon.utils.get import get_path_params, get_name_params


@app.route('/touch/', methods=['POST'])
def touch_route():
    try:
        touch(
            get_path_params(request.args),
            get_name_params(request.args)
        )
        return {}
    except Exception as e:
        return error(e)
