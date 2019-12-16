# 更改文件权限
import os, sys, stat

# 设置只读属性
os.chmod("hello.txt", stat.S_IREAD)

# 设置写属性
os.chmod("hello.txt", stat.S_IWRITE)

print("修改成功!!")
