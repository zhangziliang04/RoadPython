# 条件语句
age = int(input("请输入你的年龄："))
if age <= 18:
    print("未成年人")
elif 18 < age < 35:
    print("青年人")
elif 35 < age < 50:
    print("中年人")
else:
    print("火星人")
