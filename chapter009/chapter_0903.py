# 模块
from chapter009.chapter_0901 import add, add1


# 主函数
def main():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    add1(a, b)


# 执行主函数
if __name__ == '__main__':
    main()