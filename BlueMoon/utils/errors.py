from flask import make_response, abort

from BlueMoon.gui.usr_interaction import show_msg

FileOrFolderNotFound = Exception("File or Folder does not exists")


def permission_denied():
    show_msg("Error", "Need elevation permissions")


def show_error(msg: str) -> None:
    show_msg("Error", "Something went wrong" if msg is None else msg)


def error(e: Exception):
    if "422" in str(e):
        insufient_args_error()
    return make_response({"error": str(e)}, 500)


def wrong_password_error():
    abort(401)


def insufient_args_error():
    abort(422)
