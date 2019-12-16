def add(a, b):
    """加法函数"""
    c = a + b
    print("add 函数：%d + %d = %d " % (a, b, c))
    return c


# 函数定义: 求和函数
def add1(a, b):
    """加法函数"""
    c = a + b
    print("add1 函数：%d + %d = %d " % (a, b, c))
    return c


def add2(a, b):
    """加法函数"""
    c = a + b
    print("add2 函数：%d + %d = %d " % (a, b, c))
    return c

# add(10, 20)


def main():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    add(a, b)


# main 函数
if __name__ == '__main__':
    print("main:", __name__)
    main()



