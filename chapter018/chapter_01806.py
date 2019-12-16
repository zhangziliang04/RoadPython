# JSON解码：
import json
# JSON数组array -> Python列表
result1 = json.loads('["Michael Jordon", "Kobe Bryant"]')
print(result1)


# JSON字符串 -> Python字符串
result2 = json.loads('"Michael Jordon"')
print(result2)


# 定义一个自定义的转化函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


# 自定义恢复函数：real数据转成复数的实部，imag转成复数的虚部
result3 = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
print(result3)
f = open('a.json')
# 从文件流恢复JSON列表
result4 = json.load(f)
print(result4)
