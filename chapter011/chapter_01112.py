# 断点调试-练一练
try:
    # 正常语句
    b = 4 + spam * 3
    print(b)
except ValueError:
    print("ValueError")
except OSError:
    print("OSError")
# 注意：未知类型，全部在此处处理
except:
    print("未知异常")
# 无以上异常，执行
else:
    print("Else")
# 无论Try子句里面有没有发生异常，finally 子句都会执行
finally:
    print("Finally")