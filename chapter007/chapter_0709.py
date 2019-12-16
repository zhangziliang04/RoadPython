# 修改文件属性，仅限Unix使用
import os
import stat

# 打开文件
fd = os.open("hello.txt", os.O_RDONLY)

# 设置文件可通过组执行
os.fchmod(fd, stat.S_IXGRP)

# 设置文件可被其他用户写入
os.fchmod(fd, stat.S_IWOTH)

print("修改权限成功!!")

# 关闭文件
os.close(fd)
