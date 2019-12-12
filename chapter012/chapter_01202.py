# 正则表达式对象（正则对象）
import re
url = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500"
pattern1 = re.compile('http')
pattern2 = re.compile('com')

# pattern.match() :从起始位置开始匹配
print("-----------------pattern.match()----------------------")
print(pattern1.match(url))
print(pattern2.match(url))

# pattern.search()
print("-----------------pattern.search()----------------------")
print(pattern1.search(url))
print(pattern2.search(url))

# pattern.findall
url2 = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500https"
print("-----------------pattern.findall()----------------------")
print(pattern1.findall(url2))

# pattern.sub
print("-----------------pattern.sub()----------------------")
print(pattern1.sub('https', url2))
