# JSON解码：从文件读取
import json

# 从文件读取
f = open('stu_info.json', encoding='utf-8')
user_dic = json.load(f)
print(user_dic)         # 打印字典
print(type(user_dic))   # 打印user_dic类型
print(user_dic.keys())  # 打印字典的所有Key

