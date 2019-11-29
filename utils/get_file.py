"""
获取文件的服务
"""
import os


def get_file(path):
    """
    获取文件的位置
    :param path: 配置文件的父目录
    :return: 绝对路径
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + path
