# -*- coding: UTF-8 -*-
# 查询数据库表
import pymysql.cursors


# 查询数据库表
def db_query():
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
            sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)

            try:
                # 执行SQL语句，返回影响的行数
                row_count = cursor.execute(sql)
                print(row_count)
                # 获取所有记录列表
                results = cursor.fetchall()
                print(results)
                for row in results:
                    # 此处不可以用索引访问：row[0]
                    fname = row["FIRST_NAME"]
                    lname = row["LAST_NAME"]
                    age = row["AGE"]
                    sex = row["SEX"]
                    income = row["INCOME"]
                    # 打印结果
                    print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income))
            except:
                print("错误：数据查询操作失败")

    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    db_query()
