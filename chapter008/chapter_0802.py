# 改变当前工作目录
import os, sys

path = "/temp"
# 查看当前工作目录
ret1 = os.getcwd()
print("当前工作目录为： %s" % ret1)
# 修改当前工作目录
os.chdir(path)

# 查看修改后的工作目录
ret2 = os.getcwd()
print("目录修改成功：%s" % ret2)


