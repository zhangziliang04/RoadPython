# 线程同步问题：同时操作全局变量的情况
import time
import threading


# 类声明
class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def run(self):
        print('-----------------start:%s--------------------' % self.getName())
        global num
        temp = num
        time.sleep(0.2)
        temp -= 1
        num = temp
        print('t_name = %s : num = %s' % (self.getName(), temp))
        print('-----------------end:%s-----------------------' % self.getName())


# 主线程
print('-------------启动：主线程------------------')
thread_lst = []
num = 10     # 全局变量
# 对象创建
for i in range(10):
    t = MyThread(name=str(i),)
    thread_lst.append(t)
    t.start()
# 等待执行
[t.join() for t in thread_lst]
print('num最后的值为：{}'.format(num))
print('-------------结束：主线程------------------')

