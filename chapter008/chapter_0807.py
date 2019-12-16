# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

# 列出当前目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 重命名文件夹
os.renames("hello.txt", "temp/111.txt")
print("重命名成功。")

# 列出重命名后的目录
print("目录为: %s" % os.listdir(os.getcwd()))
