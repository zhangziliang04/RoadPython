# -*- coding: UTF-8 -*-
import os
import csv
import sys
import pymysql.cursors
import time

def txtRead():
    with open("D:\\work\\code\\mysql\\text_data_1.txt",'r',encoding='UTF-8') as txtfile:
        lines = txtfile.readlines()
        for line in lines:
            line = line.strip().split("\t")
            print(line[0])
'''
import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='woider',
    passwd='3243',
    db='python',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('雷军', '13512345678', 10000)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')

# 查询数据
sql = "SELECT name,saving FROM trade WHERE account = '%s' "
data = ('13512345678',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')

# 事务处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()

'''


def load2mysql():
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='zhangzl',
        db='login',
        charset='utf8'
    )

    # 获取游标
    cursor = connect.cursor()
    #读取文件
    with open("D:\\work\\code\\mysql\\text_data_1.txt",'r',encoding='UTF-8') as txtfile:
        lines = txtfile.readlines()

        i = 0
        for line in lines:
            line = line.strip().split("\t")
            start = time.time()
            sql = "INSERT INTO login (userid, errorcode, actiontype) VALUES ( '%s', '%s', %s )"
            data = (line[0],line[1],line[2])
            cursor.execute(sql % data)

            i = i + 1
            if(i%20000 == 0):
                connect.commit()
                print("提交：%d",i)
                end = time.time()
                print("成功插入记录:",";所用时间:",(end - start),"秒");
            #print(line)
    # 插入数据i
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')
    # 关闭连接
    cursor.close()
    connect.close()
if __name__=="__main__":
    # 管理系统路径
    sys.path.append("../")
    load2mysql()
    print("处理结束")
