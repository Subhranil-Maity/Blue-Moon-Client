import getpass
import json
import os
import sys
from flask import *
import psutil

app = Flask(__name__)
pwd = ""


# %3A = :
# %5C = \
# %5E = ^
def create_pwd():
    pd = getpass.getpass("New Password: ")
    if pd == getpass.getpass("Confirm Password: "):
        pwd = pd
        with open("config.json", 'w') as helo:
            helo.write(json.dumps({"pwd": pd}))
        return
    print('Password did not match')
    create_pwd()


with open("config.json", 'r') as handle:
    try:
        pwd = json.loads(handle.read())['pwd']
    except:
        create_pwd()


def check_pwd(passd):
    if pwd == passd:
        return True
    else:
        return False


'''
codes:
0   All Ok
1   Incorrect Password
2   File or Folder does not exists
999 Unknown Or Random
'''


def returnCode(code: int, msg: str = None):
    if msg is None: msg = ""
    if code == 1: msg = "Incorrect Password"
    if code == 2: msg = "File or Folder does not exists"
    if code == 999:
        pass
    else:
        msg = "Unknown Error" if msg == "" else msg
    return {
        "code": code,
        "msg":  msg
    }



def returnDir(loc: str):
    if not loc.endswith("\\"): loc += "\\"
    items = []
    for item in os.listdir(loc):
        if os.path.isfile(loc + item):
            types = "file"
        elif os.path.isdir(loc + item):
            types = "folder"
        else:
            types = "unknown"
        items.append({
                "name": item,
                "type": types,
                "size": -1 if not os.path.isfile(loc + item) else os.path.getsize(loc + item)
        })
    return {
        "path": loc,
        "content": items,
        "code": 0
    }


@app.route('/')
def root():
    return {
        "Name": os.environ['COMPUTERNAME']
    }


@app.route('/dir/<string:pwd>/<string:loc>', methods=['GET'])
def get_dir(pwd: str, loc):
    try:
        if not check_pwd(pwd): return returnCode(1)
        if not os.path.isdir(loc): return returnCode(2)
        return returnDir(loc)
    except Exception as e:
        return returnCode(e)


@app.route('/mkdir/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def mkdir(pwd, loc, name):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("mkdir " + loc + "\\" + name)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))


@app.route('/mkdir/<string:pwd>/<string:locname>', methods=['GET'])
def mkdir_whole(pwd, locname):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("mkdir " + locname)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))


@app.route('/touch/<string:pwd>/<string:loc>/<string:name>', methods=['GET'])
def touch(pwd, loc, name):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("type nul >>" + loc + "\\" + name)
        return returnCode(0)
    except Exception as e:
        returnCode(999, str(e))


@app.route('/touch/<string:pwd>/<string:locname>', methods=['GET'])
def touch_whole(pwd, locname):
    if not check_pwd(pwd): return returnCode(1)
    try:
        os.system("type nul >>" + locname)
        return returnCode(0)
    except Exception as e:
        returnCode(999, str(e))


@app.route('/delete/<string:pwd>/<string:path>', methods=['GET'])
def delete(pwd, path: str):
    if not check_pwd(pwd): return returnCode(1)
    try:
        if os.path.isdir(path):
            os.system("rmdir /q /s " + path)
        elif os.path.isfile(path):
            os.system("del /f " + path)
        else:
            return returnCode(2)
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))


@app.route('/type/<string:pwd>/<string:path>', methods=['GET'])
def getType(pwd, path):
    if not check_pwd(pwd): return returnCode(1)
    try:
        with open(path, 'r') as handle:
            data = handle.read()
        return returnCode(0)
    except Exception as e:
        return returnCode(999, str(e))


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


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        app.run(debug=True if "-d" in sys.argv else False, host=sys.argv[1], port=int(sys.argv[2]))
    else:
        app.run(debug=True if "-d" in sys.argv else False, host='0.0.0.0', port=5555)
