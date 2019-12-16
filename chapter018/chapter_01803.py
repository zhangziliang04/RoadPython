# JSON编码：dumps
import json

student = {'萧景瑞': '公子榜第二名', '萧景琰': '靖王'}
res2 = json.dumps(student, indent=8, ensure_ascii=False)
print(res2)

with open('stus1.json', 'w', encoding='utf-8') as f:       # 使用.dumps()方法时，要写入
    f.write(res2)
