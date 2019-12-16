# JSON编码：dump
import json

student = {'萧景瑞': '公子榜第二名', '萧景琰': '靖王'}
f = open('stus2.json', 'w', encoding='utf-8')

json.dump(student, f, indent=4, ensure_ascii=False)
f.close()
