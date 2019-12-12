# 信号量：无信号量的情况
"""
场景描述：有10个人吃饭，但只有一张餐桌，只允许做3个人，没上桌的人不允许吃饭，已上桌吃完饭离座之后，
下面的人才能抢占桌子继续吃饭，如果不用信号量，肯定是10人一窝蜂一起吃饭.
"""
from threading import Thread
import time
import random


# 线程：
class MyThread(Thread):
    def __init__(self, name=None, customer=None):
        super().__init__()
        self.name = name
        self.custom = customer

    def run(self):
        print('{}号顾客：上座，开始吃饭'.format(self.custom))
        time.sleep(random.random())
        print('{}号顾客：离座，吃完饭了'.format(self.custom))


# 主函数
if __name__ == '__main__':
    for i in range(20):
        p = MyThread("线程%d" % i, i)
        p.start()
