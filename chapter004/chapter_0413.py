# 可命名元组
import collections
# 通过namedtuple自定义一个TupleName类
TupleName=collections.namedtuple('TupleName',['a','b','c'])
# 通过类创建对象obj
obj = TupleName(11, 22, 33)
print(obj)

