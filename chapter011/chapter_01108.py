# 主动抛出异常
try:
    raise NameError('NameError Message')
except NameError:
        print('NameError Message Except!')

