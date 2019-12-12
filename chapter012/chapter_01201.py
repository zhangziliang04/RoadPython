# 模块函数:直接匹配
import re
url = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500"

# re.match() :从起始位置开始匹配
print("-----------------re.match()----------------------")
print(re.match('http', url))
print(re.match('com', url))

# re.search()
print("-----------------re.search()----------------------")
print(re.search('http', url))
print(re.search('com', url))

# re.findall
url2 = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500https"
print("-----------------re.findall()----------------------")
print(re.findall('http', url2))

# re.sub
print("-----------------re.sub()----------------------")
print(re.sub('http', 'https', url))
