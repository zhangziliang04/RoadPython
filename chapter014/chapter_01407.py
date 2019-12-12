# 死锁问题：两个互斥锁，科学家吃面模型 - 只有一副餐具，同时四个线程
import time
from threading import Lock
from threading import Thread


# 吃面函数1：先拿面
def eatNoodles_1(noodle_lock, fork_lock, scientist):
    noodle_lock.acquire()
    print('{} ：拿到了面'.format(scientist))
    fork_lock.acquire()
    print('{} ：拿到了叉子'.format(scientist))
    time.sleep(1)
    print('{} ：吃到了面'.format(scientist))
    fork_lock.release()
    noodle_lock.release()
    print('{} ：放下了面'.format(scientist))
    print('{} ：放下了叉子'.format(scientist))


# 吃面函数2：先拿叉子
def eatNoodles_2(noodle_lock, fork_lock, scientist):
    fork_lock.acquire()
    print('{}： 拿到了叉子'.format(scientist))
    noodle_lock.acquire()
    print('{}：拿到了面'.format(scientist))
    print('{}：吃到了面'.format(scientist))
    noodle_lock.release()
    print('{}：放下了面'.format(scientist))
    fork_lock.release()
    print('{}：放下了叉子'.format(scientist))


# 科学家列表
list1 = ['霍金', '居里夫人']
list2 = ['爱因斯坦', '富兰克林']
# 面条锁
noodle_lock = Lock()
# 叉子锁
fork_lock = Lock()
# 线程组1：两个线程
for i in list1:
    t = Thread(target=eatNoodles_1, args=(noodle_lock, fork_lock, i))
    t.start()
# 线程组2：两个线程
for i in list2:
    t = Thread(target=eatNoodles_2, args=(noodle_lock, fork_lock, i))
    t.start()
