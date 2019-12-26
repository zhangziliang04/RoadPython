# -*- coding: UTF-8 -*-
# 数据删除操作
import pymysql.cursors


# 数据删除
def db_delete():
    # 连接到数据库
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='zhangzl',
                                 db='my_db',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:     # 基于with，不需要执行cursor.close()
            # SQL 插入语句
            sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

            try:
                # 执行SQL语句,返回影响的行数
                row_count = cursor.execute(sql)
                # 提交修改：不可调用游标的cursor.commit
                connection.commit()
                print('数据删除成功，影响行数：%d' % row_count)
            except:
                # 回滚操作
                print("数据删除异常：执行回滚")
                connection.rollback()
    finally:
        connection.close()


# 执行主函数
if __name__ == '__main__':
    db_delete()
