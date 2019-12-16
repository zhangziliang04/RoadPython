# 根据文件，修改当前目录
import os

# 输出当前目录
print("当前工作目录为 : %s" % os.getcwd())

# 打开新目录 temp2
fd = os.open("temp2/hello.txt", os.O_RDONLY)

# 修改当前目录
os.fchdir(fd)
# 输出当前目录
print("当前工作目录为 : %s" % os.getcwd())
# 关闭打开的目录
os.close(fd)
