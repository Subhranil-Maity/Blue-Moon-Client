from BlueMoon.gui.usr_interaction import show_msg


def permission_denied():
    show_msg("Error", "Need elevation permissions")

def show_error(msg: str) -> None:
    show_msg("Error", "Something went wrong" if msg is None else msg)
