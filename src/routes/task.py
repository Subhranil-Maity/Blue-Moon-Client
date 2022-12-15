from src.app import app
from src.utils.auth import *
from src.utils.functions import *
import os
import psutil

@app.route('/gettask/<string:pwd>/', methods=['GET'])
def get_task(pwd):
    if not check_pwd(pwd): return returnCode(1)
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
        return returnCode(999, str(e))

