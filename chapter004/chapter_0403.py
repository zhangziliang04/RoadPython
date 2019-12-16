# 数据类型程序实例3：数值类型
# 01：创建变量
print("------------变量初始化-------------")
val1 = 10
val2 = 10.22
val3 = 10+4j
val4 = True

# 02：类型判定
print("------------类型判定-------------")
print(type(val1),type(val2),type(val3),type(val4))
val5 = 11
print(isinstance(val5,int))

# 03：删除对象引用
print("------------删除对象引用-------------")
val6 = 14
del val6
# print(val6) # 抛出异常

# 04 ：数值计算
print("------------数值计算-------------")
val1 = 10
val2 = 12
val3 = val1 + val2
print(val3)
