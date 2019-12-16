# 文件读取
import os, sys

# 打开文件
fd = os.open("hello.txt", os.O_RDWR)

# 读取文本
result = os.read(fd, 12)
print(result)

# 关闭文件
os.close(fd)
print("关闭文件成功!!")
