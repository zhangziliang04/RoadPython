# 字符串
str = 'Python全栈工程师'

# 索引
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
# 连接
print(str + "魔鬼训练营")
# 转义
print("换行\r\n")
print("Tab制表符\t")

# 成员运算符
if 'P' in str:
    print("P is in ", str)
# 格式化符
print("PI = %.2f" % 3.1415926)
