# -*- coding: UTF-8 -*-
# 插入数据
import pymysql.cursors


# 插入数据记录
def db_insert():
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
            # SQL 插入语句
            sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                     LAST_NAME, AGE, SEX, INCOME)
                     VALUES ('张', 'Python2', 25, 'M', 2000)"""

            # 执行SQL操作
            try:
                nrow = cursor.execute(sql)
                # 返回1代表成功
                if nrow == 1:
                    print("数据插入成功！")
                connection.commit()
            except:
                connection.rollback()
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    db_insert()
