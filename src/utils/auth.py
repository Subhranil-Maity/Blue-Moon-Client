import json
import getpass

pwd: str = ""


def check_pwd(passd):
    if pwd == "":
        create_pwd()
    if pwd == passd:
        return True
    else:
        return False


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
