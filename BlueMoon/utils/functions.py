import os


def return_code(
        code: int,
        msg: str = None,
        extras: any = None,
        data: any = None):
    return "error"
    # if msg is None: msg = ""
    # if code == 1: msg = "Incorrect Password"
    # if code == 2: msg = "File or Folder does not exists"
    # if code == 999:
    #     pass
    # else:
    #     msg = "Unknown Error" if msg == "" else msg
    # return {
    #     "code": code,
    #     "msg": msg,
    #     extras: data
    # }


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
        "code": 0,
        "msg": ""
    }
