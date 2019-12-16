# 默认字典：
from collections import defaultdict
values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# defaultdict(必须为callable一个可调用的)
my_dict = defaultdict(list)
for value in values:
    if value > 66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)

# 如果key不存在返回None
print(my_dict['k3'])
