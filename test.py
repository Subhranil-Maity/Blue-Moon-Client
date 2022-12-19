import requests
import os
import json
from urllib.parse import quote

testdir = "testdir"
baseurl = "http://127.0.0.1:5555/"
pwd = "admin"
print(__file__)

def run_task(current: int, total: int, name: str, pogress: str) -> str:
    return f"[{current}] {name} : {pogress}"


def task_dir() -> None:
    dir_tasks = [
        "c:",
        "c:/Users",
        "c:/users/fight",
    ]
    for dir_task in dir_tasks:
        req = requests.get(f"{baseurl}dir/{pwd}/{quote(dir_task)}").json()
        items = []
        for item in os.listdir(dir_task):
            if os.path.isfile(dir_task + item):
                types = "file"
            elif os.path.isdir(dir_task + item):
                types = "folder"
            else:
                types = "unknown"
            curr = {
                "name": item,
                "type": types,
                "size": -1 if not os.path.isfile(dir_task + item) else os.path.getsize(dir_task + item)
            }
            if curr not in req['content']:
                print("error")
