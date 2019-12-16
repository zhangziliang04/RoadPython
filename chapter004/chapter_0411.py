# 有序字典:记住了项目的插入顺序
# 重要：python3.6+ dict类型，默认支持按照插入顺序记录元素，不需要额外的OrderDict
from collections import OrderedDict

# 普通字典
d = dict([('a', 1), ('c', 3), ('b', 2), ('d', 4), ('e', 5), ('f', 6)])
print(d)

items = d.items()
# items.sort() # python3.x 版本items返回类型不是列表，不支持sort
items = sorted(items)

for key, value in items:
    print(key, value) # print key,dict[key]

# 有序字典:Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])   #
print(od)

items = od.items()
items = sorted(items)
for key, value in items:
    print(key, value) # print key,dict[key]

# 更新元素：不存在是新增
od.update({'a':'5'})
print(od)

# 移动到尾部
od.move_to_end('a')
print(od)

# 删除元素
od.pop('a')     # 指定元素
print(od)
od.popitem()    # 有序删除:右侧
print(od)
od.clear()      # 清空
print(od)
