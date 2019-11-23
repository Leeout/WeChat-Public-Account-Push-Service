"""
按照编程规范，所有需要打印的地方，需要调用本文件的logger，此处logger与logging的区别是，
logger在打印时根据不同的打印级别显示不同的颜色
"""
import logging
import colorlog

LOG_LEVEL = logging.NOTSET
# https://pypi.org/project/colorlog/

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(name)s:%(message)s'))
logger = colorlog.getLogger()
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)