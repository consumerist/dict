"""
operation.py
数据库操作模块
思路：
将数据库操作封装成一个类，将dict_server.py需要地数据库功能分别写成方法，在dict_server实例话对象，需要
什么方法直接调用
"""
import pymysql


class Database:
    def __init__(self,
                 database=None,
                 host="localhost",
                 port=3306,
                 user="root",
                 password="nsmsmdwyzwy21",
                 charset="utf8"):
        self.cur = None
        self.db = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.Connect()

    def Connect(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset=self.charset)

    def Cursor(self):
        self.cur = self.db.cursor()

    def Search(self, user, pwd):
        sql = "select * from user where name = %s"
        self.cur.execute(sql, [user, ])
        result = self.cur.fetchone()
        if result:
            return False
        else:
            try:
                sql = "insert into user (name , password) values (%s,%s)"
                self.cur.execute(sql, [user, pwd])
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print(e)
                return False
            else:
                return True

    def log(self, user, pwd):
        sql = "select * from user where name = %s and password = %s"
        self.cur.execute(sql, [user, pwd])
        result = self.cur.fetchone()
        if result:
            return True
        else:
            return False
    def close(self):
        self.db.close()
