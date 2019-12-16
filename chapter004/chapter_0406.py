# Python数据类型之元组
# 01：创建
tuple = ("北京","深圳",50)
print(tuple)

#02: 元素访问
tuple = ("北京","深圳","上海","天津","雄安新区")
print(tuple[0])
print(tuple[1:3])


# 03:修改元组
tup1 = ("北京","深圳","上海","天津")
tup2 = ("雄安新区",)
tup3 = tup1 + tup2
print(tup3)

# 04:删除元祖
tup = ("北京","深圳","上海","天津")
print(tup)
# del tup[0]
del tup
# print(tup)  #抛出异常