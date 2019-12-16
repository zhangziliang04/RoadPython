# 文件&文件夹 访问权限验证
import os, sys
# 假定 hello.txt 文件存在，并有读写权限；
# 注意：如果文件不存在，显示为False
# 01.是否存在
ret = os.access("./temp", os.F_OK)
print("F_OK - 返回值 %s" % ret)

# 02.是否可读
ret = os.access("111.txt", os.R_OK)
print("R_OK - 返回值 %s" % ret)

# 03. 是否可写
ret = os.access("hello.txt", os.W_OK)
print("W_OK - 返回值 %s" % ret)

# 04. 是否可执行
ret = os.access("hello.txt", os.X_OK)
print("X_OK - 返回值 %s" % ret)
