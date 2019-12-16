# 类的声明
class MyClass:
    """类注释部分 """
    # 成员变量
    age = None
    name = None

    # 成员函数
    def get_age(self):
        print(self.age)
        return self.age

    def set_age(self, age):
        self.age = age
        print(age)


def main():
    # 无参数的对象声明
    mycls = MyClass()
    print(mycls.age)
    mycls.get_age()
    mycls.set_age(10)
    print(mycls.age)


# 执行主函数
if __name__ == '__main__':
    main()






