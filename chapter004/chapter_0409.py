# 扩展类型：
#
# 双向队列
import collections

# 对象声明
deq = collections.deque('abcd')
print(deq)

# 01.添加元素 - 右侧
deq.append(11)
print(deq)

# 01.添加元素 - 左侧
deq.appendleft(12)
print(deq)

# 01.添加元素 - 指定位置插入元素
deq.insert(4, 44)

# 02.队列拓展 - 右侧
deq.extend([11, 22, 33])
print(deq)

# 02.队列拓展 - 左侧
deq.extendleft([11, 22, 33])
print(deq)

# 03.取元素索引位置
print(deq.index('a'))

# 04.移除元素
print(deq)
deq.pop()       # 右侧
deq.popleft()   # 左侧
deq.remove('a') # 指定元素
deq.rotate(-2)  # N < 0 左侧移除；N > 0 右侧移除
print(deq)

# 05.队列反转
deq.reverse();
print(deq)

# 06.元素
# 清空队列
deq.clear()
print(deq)



