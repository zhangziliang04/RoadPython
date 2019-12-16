# 01：添加数据，单个元素，可以是任意类型
myset = {"北京","上海","天津"}
myset.add("深圳")
print(myset)
# {'上海', '北京', '天津', '深圳'}
# 添加元素：允许-元组、列表、词典、集合；不允许-数字、字符串
myset.update("雄安新区")
print(myset)
# {'安', '区', '上海', '北京', '新', '天津', '雄', '深圳'}
myset.update({"雄安新区"})
print(myset)
# {'安', '区', '上海', '北京', '新', '天津', '雄', '雄安新区', '深圳'}


# 02：删除数据
print("-----------删除元素--------------")
# 方法1：remove(x)
myset = {"北京","上海","天津"}
print(myset)
myset.remove("北京")
print("北京")
print(myset)
# 删除不存在元素，报异常
myset.remove("北京")

# 方法2：discard(x)
myset = {"北京","上海","天津"}
print(myset)
myset.discard("北京")
print(myset)
# 删除不存在的元素，无提示
myset.discard("北京")
print(myset)

# 方法3：pop() 随机删除

myset = {"北京","上海","天津"}
print(myset)
myset.pop()
print(myset)
myset.pop()
print(myset)
myset.pop()
print(myset)
# 无元素可删除时，程序异常
# myset.pop()

# 03：计算集合元素个数
print("-----------计算元素个数--------------")
myset = {"北京","上海","天津"}
print(len(myset))

# 4：判断元素是否在集合中
print("-----------判断元素是否在集合中--------------")
myset = {"北京","上海","天津"}
print("北京" in myset)
print("广州" in myset)

# 5：集合元素访问
print("-----------访问集合中元素--------------")
# print(myset[1])    # 异常：不支持索引访问
lst = list(myset)
print(lst[0])



