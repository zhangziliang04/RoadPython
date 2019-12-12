# 线程创建：基于面向对象
import os
import time
import threading


# 自定义线程类
class MyThread(threading.Thread):
    def __init__(self, n, name=None):
        super().__init__()
        self.name = name
        self.n = n

    def run(self):
        print('-------start:---------')
        time.sleep(1)
        my_thread_name = threading.current_thread().name
        my_thread_id = threading.current_thread().ident
        print('当前线程为：{}，线程id为：{}，所在进程为：{},您输入的参数为：{}'.format(my_thread_name,
                                                             my_thread_id, os.getpid(), self.n))
        print('--------end------------')


# 对象创建
mythread = MyThread(name='线程1', n=1)
mythread.start()
time.sleep(2)

# 主线程信息
main_thread_name = threading.current_thread().name
main_thread_id = threading.current_thread().ident
print('主线程为：{}，线程id为：{}，所在进程为：{}'.format(main_thread_name ,main_thread_id , os.getpid()))