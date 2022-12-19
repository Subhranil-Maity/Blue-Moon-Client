from BlueMoon.app import config

def check_pwd(passd):
    if passd is None:
        return False
    if config.check_pwd(passd):
        return True
    else:
        return False
