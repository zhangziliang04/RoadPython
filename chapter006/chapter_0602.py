# 字符串格式控制
mystr = "Python全栈工程师"
print("str:", str(mystr))
print("repr:", repr(mystr))
print("str(int):", str(1/4))

# % 格式说明
PI = 3.1415926
print("PI-整型：%2d" % PI)
print("PI-字符串：%s" % PI)
print("PI-浮点数：%f" % PI)
print("PI-两位小数：%.2f" % PI)
print("指定占位符宽度(左对齐):%-5.2f" % PI)
print("字符串截取：%.2s" % PI)


# str.format()
print("------str.format()----------")
print("PI-整型：{}".format(PI))
print("PI-实数：{0:f}".format(PI))
print("PI-两位小数：{0:.2f}".format(PI))
print("PI-指定占位符宽度：{0:5.2f}".format(PI))



