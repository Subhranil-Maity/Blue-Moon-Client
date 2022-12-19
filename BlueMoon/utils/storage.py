import getpass
import os
import pickle
import hashlib

from BlueMoon.utils.errors import permission_denied, show_error


class Config:
    pwd: str
    tokens: list

    def __init__(self):
        self.new_config()

    def check_pwd(self, pwd: str) -> bool:
        return self.hash(pwd) == self.pwd

    def hash(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def accept_new_pwd(self) -> None:
        pd = getpass.getpass("New Password: ")
        if pd == getpass.getpass("Confirm Password: "):
            self.pwd = self.hash(pd)
            return None
        self.accept_new_pwd()

    def save_config(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), "config.pkl") , 'wb') as config:
                pickle.dump(self, config)
        except PermissionError:
            permission_denied()
            exit(101)
        except Exception as e:
            show_error(e)

    def new_config(self):
        self.accept_new_pwd()
        self.tokens = []

        self.save_config()


def load_config() -> Config:
    if os.path.exists(os.path.join(os.path.dirname(__file__), "config.pkl")):
        with open(os.path.join(os.path.dirname(__file__), "config.pkl"), "rb") as f:
            return pickle.load(f)
    else:
        print("No Config found")
        return Config()
