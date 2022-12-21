from BlueMoon.app import config
from BlueMoon.utils.errors import insufient_args_error, wrong_password_error


def check_password(args):
    if "pwd" not in args:
        insufient_args_error()
    elif args.get("pwd") is None:
        wrong_password_error()
    elif not config.check_pwd(args.get("pwd")):
        wrong_password_error()