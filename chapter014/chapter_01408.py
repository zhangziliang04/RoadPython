# 递归锁：此处用一个锁，可重入
import time
import threading
from threading import RLock


# 类声明
class MyThread1(threading.Thread):
    def __init__(self, name=None, noodlelock=None, forklock=None, scientist = None):
        super().__init__()
        self.name = name
        self.noodle_lock = noodlelock
        self.fork_lock = forklock
        self.scientist = scientist

    def run(self):
        print('-----------------start:%s--------------------' % self.getName())
        # 获取锁：
        noodle_lock.acquire()
        print('{} ：拿到了面'.format(self.scientist))
        fork_lock.acquire()
        print('{} ：拿到了叉子'.format(self.scientist))
        time.sleep(1)
        print('{} ：吃到了面'.format(self.scientist))
        fork_lock.release()
        noodle_lock.release()
        print('{} ：放下了面'.format(self.scientist))
        print('{} ：放下了叉子'.format(self.scientist))
        print('-----------------end:%s-----------------------' % self.getName())


# 类声明
class MyThread2(threading.Thread):
    def __init__(self, name=None,noodlelock=None, forklock=None, scientist=None):
        super().__init__()
        self.name = name
        self.noodle_lock = noodlelock
        self.fork_lock = forklock
        self.scientist = scientist

    def run(self):
        print('-----------------start:%s--------------------' % self.getName())
        self.fork_lock.acquire()
        print('{}： 拿到了叉子'.format(self.scientist))
        self.noodle_lock.acquire()
        print('{}：拿到了面'.format(self.scientist))
        print('{}：吃到了面'.format(self.scientist))
        self.noodle_lock.release()
        print('{}：放下了面'.format(self.scientist))
        self.fork_lock.release()
        print('{}：放下了叉子'.format(self.scientist))
        print('-----------------end:%s-----------------------' % self.getName())


# 科学家列表
list1 = ['霍金', '居里夫人']
list2 = ['爱因斯坦', '富兰克林']
# 面条锁
noodle_lock = fork_lock = RLock()
# 叉子锁
# fork_lock = RLock()
# 线程组1：两个线程
for i in list1:
    t = MyThread1("线程1", noodle_lock, fork_lock, i)
    t.start()
# 线程组2：两个线程
for i in list2:
    t = MyThread2("线程2", noodle_lock, fork_lock, i)
    t.start()
