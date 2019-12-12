# 互斥锁：
import time
import threading
from threading import Thread
from threading import Lock


# 类声明
class MyThread(threading.Thread):
    def __init__(self, name=None, lock=None):
        super().__init__()
        self.name = name
        self.lock = lock

    def run(self):
        print('-----------------start:%s--------------------' % self.getName())
        # 获取锁：
        self.lock.acquire()
        global num
        temp = num
        time.sleep(0.2)
        temp -= 1
        num = temp
        print('t_name = %s : num = %s' % (self.getName(), temp))
        # 释放锁：
        self.lock.release()
        print('-----------------end:%s-----------------------' % self.getName())


# 主线程
print('-------------启动：主线程------------------')
lock1 = threading.Lock()
thread_lst = []
num = 10     # 全局变量

# 对象创建
for i in range(5):
    t = MyThread(name=str(i),lock=lock1)
    thread_lst.append(t)
    t.start()
# 等待执行
[t.join() for t in thread_lst]
print('num最后的值为：{}'.format(num))
print('-------------结束：主线程------------------')

