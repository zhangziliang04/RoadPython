# 文件描述符复制
import os, sys
# 打开文件
fd = os.open("hello.txt", os.O_RDWR | os.O_CREAT)
# 复制文件描述符
d_fd = os.dup(fd)
# 使用复制的文件描述符写入文件
os.write(d_fd, "基于文件描述符复制，写入测试".encode())
# 关闭文件
os.closerange(fd, d_fd)
print("关闭所有文件成功!!")
