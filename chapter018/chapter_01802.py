# 解码：从字符串
import json
f = open('stu_info.json', encoding='utf-8')

# 使用loads()方法，需要先读文件
content = f.read()
user_dic = json.loads(content)
# 输出JSON内容
print(user_dic)         # 打印字典
print(type(user_dic))   # 打印user_dic类型
print(user_dic.keys())  # 打印字典的所有Key
