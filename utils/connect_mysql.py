import pymysql
from utils.logger import logger


class ConnectMysql:
    def __init__(self, host, user, password, db_name, sql):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.sql = sql

    def connect_mysql(self):
        try:
            db = pymysql.connect(self.host, self.user, self.password, self.db_name)
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # 执行SQL语句
            cursor.execute(self.sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results

        except Exception as error:
            logger.error("mysql连接失败，原因：%s", error)

    def select_table(self, i):
        sql = self.connect_mysql()
        return sql[i]
