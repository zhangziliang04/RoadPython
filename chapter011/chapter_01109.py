# 自定义异常类型: 基于Exception类派生
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
# 异常捕获
try:
    raise MyError("MyError Message")
except NameError:
    print('NameError Message Except!')
except MyError as error:
    print('MyError Message Except:',error.value)