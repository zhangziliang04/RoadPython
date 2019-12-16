# 类的继承
class BaseClass:
    """基类"""
    # 成员变量
    def __init__(self, age, name, job):   # 特殊函数：双下划线开始+双下划线结束，系统定义的特殊函数，不能在类外部访问
        self.age = age          # 公有成员: 对所有人公开，可以在类的外部直接访问
        self._name = name       # 保护成员：不能够通过 "from module import *" 的方式导入
        self.__job = job        # 私有成员：双下划线开始，无双下划线结束；类的外部不能直接访问，需要调用类的公开成员方法访问

        print("BaseClass init")

    # 成员函数
    def get_age(self):
        print(self.age)
        return self.age

    def set_age(self, age):
        self.age = age
        print(age)
    # 保护成员函数
    def _get_name(self):
        return self._name

    # 私有成员函数
    def __get_job(self):
        return self.__job


# 派生类
class DriverdClass(BaseClass):
    def __init__(self, age, name, job, cardno):
        BaseClass.__init__(self, age, name, job)
        self.cardno = cardno
        print("DriverdClass init")

    def get_age(self):
        print("DriverdClass get_age")


def main():
    # 有参数的对象声明
    mycls = DriverdClass(20, "张子良", "Python全栈工程师", "SVIP_0001")
    mycls.get_age()         # 增加重载的情况
    print(mycls._name)
    mycls._get_name()       # 访问保护成员函数


# 执行主函数
if __name__ == '__main__':
    main()