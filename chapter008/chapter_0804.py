# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

# 更改当前进程的根目录为指定的目录，使用该函数需要管理员权限
# 设置根目录为 /temp
os.chroot("/temp")
print("修改根目录成功!!")