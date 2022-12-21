from BlueMoon.utils.errors import insufient_args_error


def get_path_params(args):
    if "path" not in args:
        insufient_args_error()
    return args.get("path")


def get_name_params(args):
    if "name" not in args:
        insufient_args_error()
    return args.get("name")
