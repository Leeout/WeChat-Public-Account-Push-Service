import os


def get_file(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + path
