# 文件写入
import os
import sys

# 打开文件
fd = os.open("hello.txt", os.O_RDWR | os.O_CREAT)

# 写入字符串
os.write(fd, str.encode("写入测试"))

# 关闭文件
os.close(fd)

print("关闭文件成功!!")
