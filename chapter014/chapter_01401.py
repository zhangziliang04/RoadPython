# 线程创建：基于自定义函数
import os
import time
import threading


# 线程执行函数
def fun(n):
    print('-------start:---------')
    time.sleep(1)
    my_thread_name = threading.current_thread().name  # 获取当前线程名称
    my_thread_id = threading.current_thread().ident  # 获取当前线程id
    print('当前线程名为：{}，线程id为：{}，所在进程为：{},参数为：{}'.format(my_thread_name, my_thread_id, os.getpid(), n))
    print('-------end:---------')


# 创建线程对象
mythread = threading.Thread(target=fun, name='线程1', args=('参数1',))
# 启动线程执行
mythread.start()
time.sleep(2)

# 主线程信息
main_thread_name = threading.current_thread().name
main_thread_id = threading.current_thread().ident
print('主线程名为：{}，线程id为：{}，所在进程为：{}'.format(main_thread_name, main_thread_id, os.getpid()))
