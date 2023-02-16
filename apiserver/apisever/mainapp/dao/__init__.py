import pymysql

CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '15737764003',
    'db': 'test',
    'charset': 'utf8',
    'cursor-class': pymysql.cursors.DictCursor
}


class DB:
    def __init__(self):
        self.conn = pymysql.Connect(**CONFIG)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None


class BaseDao():
    def __int__(self):
        self.db = DB()

    def find_all(self, table, where=None, **whereArgs):
        sql = 'select * from %s' % table
        if where:
            sql += where
        with self.db as c:
            c.execute(sql, whereArgs)
            result = list(c.fetchall())
        return result

    def __del__(self):
        pass
