# 文件写入
import os, sys

# 打开文件
fd = os.open("hello.txt", os.O_RDWR | os.O_CREAT)

# 写入字符串
str1 = "This is a Test"
ret = os.write(fd, bytes(str1, 'GBK'))

# 输入返回值
print("写入的位数为: ", ret)
print("内容写入成功")

# 关闭文件
os.close(fd)
print("关闭文件成功!!")
