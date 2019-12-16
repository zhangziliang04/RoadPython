# -*- coding: UTF-8 -*-
import pymysql.cursors

#连接到数据库
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='zhangzl',
                             db='my_db',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        #查看全部数据库
        sql = "show databases"
        dbs = cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
    # connection is not autocommit by default. So you must commit to save
    connection.commit()
    with connection.cursor() as cursor:
        # 查看所有表
        sql = "show tables"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()