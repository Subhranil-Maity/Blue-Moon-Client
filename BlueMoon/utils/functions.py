import os
from flask import abort, make_response, send_file

from BlueMoon.utils.errors import error, FileOrFolderNotFound


def return_code(
        code: int,
        msg: str = None,
        extras: any = None,
        data: any = None):
    return make_response("error", 500)
    # if msg is None: msg = {}
    # if code == 1: msg = "Incorrect Password"
    # if code == 2: msg = "File or Folder does not exists"
    # if code == 999:
    #     pass
    # else:
    #     msg = "Unknown Error" if msg == {} else msg
    # return {
    #     "code": code,
    #     "msg": msg,
    #     extras: data
    # }


def delete(path: str):
    if os.path.isdir(path):
        os.system("rmdir /q /s " + path)
    elif os.path.isfile(path):
        os.system("del /f " + path)
    else:
        return {}
    return {}


def return_dir(path: str):
    path = path.replace("/", "\\")
    if not path.endswith("\\"):
        path += "\\"
    items = []
    for item in os.listdir(path):
        if os.path.isfile(path + item):
            types = "file"
        elif os.path.isdir(path + item):
            types = "folder"
        else:
            types = "unknown"
        items.append({
            "name": item,
            "type": types,
            "size": -1 if not os.path.isfile(path + item) else os.path.getsize(path + item),
            "path": path + item
        })
    return items


def get_dir(path: str):
    if not os.path.isdir(path):
        return error(FileOrFolderNotFound)
    return return_dir(path)


def get_file(path: str):
    name = path.split('\\')
    return send_file(
        open(path, 'rb'),
        mimetype=None,
        download_name=name[len(name) - 1]
    )


def mkdir(path: str, name: str):
    os.system("mkdir " + path + "\\" + name)
    return {}


def touch(path: str, name: str):
    os.system("type nul >>" + path + "\\" + name)


def log(logable: str):
    print(logable)
