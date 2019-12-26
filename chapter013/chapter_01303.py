# -*- coding: UTF-8 -*-
# 创建数据库表
import pymysql.cursors


# 创建数据库表
def db_createtable():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='zhangzl',
                                 db='my_db',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # 使用 execute() 方法执行 SQL，如果表存在则删除
            cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
            # 使用预处理语句创建表
            sql = """CREATE TABLE EMPLOYEE (
                     FIRST_NAME  CHAR(20) NOT NULL,
                     LAST_NAME  CHAR(20),
                     AGE INT,  
                     SEX CHAR(1),
                     INCOME FLOAT )"""
            # 执行SQL操作
            dbs = cursor.execute(sql)
            connection.commit()
            # 查看所有表
            sql = "show tables"
            cursor.execute(sql)
            for result in cursor.fetchall():
                print(result)
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    db_createtable()
