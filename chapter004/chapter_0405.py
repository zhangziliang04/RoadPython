# 数据类型程序实例5：列表
# 01：创建变量
list = ["北京","上海","天津","深圳"]
print(list)

# 02：访问元素
list = ["北京","上海","天津","深圳"]
print(list[0])
print(list[1:3])

# 03：更新列表
print("------------更新操作-------------")
list = ["北京","上海","天津","深圳"]
list[0] = "南京"
print(list)
list.append("雄安新区")
print(list)
list2 = ["南京","石家庄"]
list = list + list2  # 列表元素允许重复
print(list)

# 04：删除操作
print("------------删除操作-------------")
list = ["北京","上海","天津","深圳"]
print(list[0])
# 删除单个元素
del list[0]
print(list)
# 删除整个列表
del list
print(list)
