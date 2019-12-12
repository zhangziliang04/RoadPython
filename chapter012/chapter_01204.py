# 正则表达式对象（正则对象）
import re
url = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500https"
pattern1 = re.compile("http")

# pattern.match() :从起始位置开始匹配
m1 = pattern1.match(url)
print(pattern1.match(url))
print(m1.group(0))
print(m1.span())

# pattern.search()
m2 = pattern1.search(url)
print(pattern1.search(url))
print(m2)


