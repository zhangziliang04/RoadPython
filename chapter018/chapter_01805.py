# JSON编码
import json
# Python元组 -> JSON列表
s1 = json.dumps(['Michael Jordon', 'Kobe Bryant'])
print(s1)

# Python字符串 -> JSON string
s2 = json.dumps('Michael Jordon')
print(s2)

# Python Dict -> JSON object
s4 = json.dumps({"Michael Jordon": 23, "Kobe Bryant": 24}, sort_keys=True)
print(s4)

# Python列表 -> JSON array
# 并指定JSON分隔符：逗号和冒号之后没有空格（默认有空格）
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
# 输出的JSON字符串中逗号和冒号之后没有空格
print(s5)

# 格式控制
# 指定indent为4：意味着转换的JSON字符串有缩进
s6 = json.dumps({'Python': 5, 'Java': 7}, sort_keys=True, indent=4)
print(s6)

# 使用JSONEncoder的encode方法将Python转JSON
s7 = json.JSONEncoder().encode({"names": ("Michael Jordon", "23")})
print(s7)
f = open('1805.json', 'w')
# 使用dump()函数将转换得到JSON字符串输出到文件
json.dump(['Kotlin', {'Python': 'excellent'}], f)