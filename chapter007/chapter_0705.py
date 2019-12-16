import os
# 打开一个文件
file = open('hello.txt', os.O_RDWR | os.O_CREAT)
# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件（stdout）
# 目标、源
os.dup2(file.fileno(), 1)
# 关闭文件
file.close()
# print 输出到标准输出流，就是文件描述符1
print('输出1')
print('输出2')
