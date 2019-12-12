# 条件变量：
import threading
import time


# 生产者线程：
class ProduceThread(threading.Thread):
    def __init__(self, name=None, con=None ):
        super().__init__()
        self.name = name
        self.con = con

    def run(self):
        # 锁定线程
        global num
        self.con.acquire()
        print("工厂开始生产……")
        while True:
            num += 1
            print("已生产商品数量：{}".format(num))
            time.sleep(1)
            if num >= 5:
                print("商品数量达到5件，仓库饱满，停止生产……")
                con.notify()  # 唤醒消费者
                con.wait()  # 生产者自身陷入沉睡
        # 释放锁
        self.con.release()


# 消费者
class ConsumerThread(threading.Thread):
    def __init__(self, name=None, con=None ):
        super().__init__()
        self.name = name
        self.con = con

    def run(self):
        con.acquire()
        global num
        print("消费者开始消费……")
        while True:
            num -= 1
            print("剩余商品数量：{}".format(num))
            time.sleep(2)
            if num <= 0:
                print("库存为0，通知工厂开始生产……")
                con.notify()  # 唤醒生产者线程
                con.wait()  # 消费者自身陷入沉睡

        con.release()


con = threading.Condition()
num = 0
p = ProduceThread("生产者线程", con)
c = ConsumerThread("消费者线程", con)
p.start()
c.start()