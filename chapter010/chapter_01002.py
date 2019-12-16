# 类的声明
class MyClass:
    """类注释部分 """
    # 初始化函数
    def __init__(self, age):
        self.age = age

    # 成员函数
    def get_age(self):
        print(self.age)
        return self.age

    def set_age(self, age):
        self.age = age
        print(age)


def main():
    # 有参数的对象声明
    mycls = MyClass(20)
    mycls.get_age()

# 执行主函数
if __name__ == '__main__':
    main()
