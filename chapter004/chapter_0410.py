# 计数器
import collections

# 对象声明
c = collections.Counter('abcdeabcdabcaba')
print(c)

# 元素访问:按照顺序输出
print(list(c.elements()))

# 增加元素重复次数
c.update('a')
print(c)

# 减少元素重复次数
c.subtract('a')
print(c)
