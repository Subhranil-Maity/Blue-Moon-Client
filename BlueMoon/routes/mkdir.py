from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
from flask import request
import os

from BlueMoon.utils.get import get_name_params, get_path_params


@app.route('/mkdir/', methods=['POST'])
def mkdir_route():
    try:
        return mkdir(
            get_path_params(request.args),
            get_name_params(request.args)
        )
    except Exception as e:
        return error(e)
