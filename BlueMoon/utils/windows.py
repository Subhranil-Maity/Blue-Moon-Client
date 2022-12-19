import ctypes
import sys


def is_admin():
    try:
        d = ctypes.windll.shell32.IsUserAnAdmin()
        return True
    except:
        return False


def go_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
