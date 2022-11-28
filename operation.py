"""
operation.py
数据库操作
"""
import pymysql

# 与数据库建立连接
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="nsmsmdwyzwy21",
                     database="dict",
                     charset="utf8")
# 创建游标对象
cur = db.cursor()


def Serach(user, pwd):
    sql = "select * from user where name = %s"
    cur.execute(sql, [user, ])
    result = cur.fetchone()
    if result:
        return False
    else:
        try:
            sql = "insert into user (name , password) values (%s,%s)"
            cur.execute(sql, [user, pwd])
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
            return False
        else:
            return True


