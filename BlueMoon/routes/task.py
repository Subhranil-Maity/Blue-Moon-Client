from BlueMoon.app import app
from BlueMoon.utils.auth import *
from BlueMoon.utils.functions import *
import os
import psutil

@app.route('/gettask/<string:pwd>/', methods=['GET'])
def get_task(pwd):
    if not check_pwd(pwd): return return_code(1)
    try:
        processes = []
        for proc in psutil.process_iter():
            processes.append({
                "name": proc.name(),
                "pid": proc.pid
            })
        return {
            "code": 0,
            "process": processes
        }
    except Exception as e:
        return return_code(999, str(e))

