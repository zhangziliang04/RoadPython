# 模块函数:直接匹配
import re
url = "http://m.study.163.com/provider/1016839500/index.htm?share=2&shareId=1016839500"

# 方法1：pattern独立存在
print("-----------------re.match()----------------------")
print(re.match('http', url))


# 方法2：pattern复用
patter1 = re.compile('http')
print(patter1.match(url))


