# 顺序语句
print("Line1")
print("Line2")
print("Line3")

# 语句 + 函数
print("顺序语句")


# 函数声明：声明时不会被调用
def fun():
    print("fun函数")


# 函数调用：顺序执行，即使有主函数
fun()

'''


# 主函数
def main():
    print("main函数执行：")
    fun()


# 执行主函数
if __name__ == '__main__':
    main()
'''