# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 移除:目录必须为空，否则异常
os.removedirs("temp")

# 列出移除后的目录
print("移除后目录为:%s" % os.listdir(os.getcwd()))
