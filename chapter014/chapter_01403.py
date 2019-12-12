# 线程对象: 属性变量 + 属性函数
import time
import threading


# 执行函数
def fun():
    print('------------启动：子线程------------------------')
    for i in range(3):
        time.sleep(1)
        my_thread_name1 = threading.current_thread().name
        print('{} - 已运行：{}秒……'.format(my_thread_name1, i + 1))
    print('------------结束：子线程------------------------')
# 主线程


print('-------------启动：主线程------------------')
mythread = threading.Thread(target=fun, name='线程1')
# 设置为守护线程
mythread.daemon = True
mythread.start()
mythread.join()
for i in range(3):
    time.sleep(1)
    my_thread_name2 = threading.current_thread().name
    print('{} - 已运行{}：秒……'.format(my_thread_name2, i + 1))
print('-------------结束：主线程------------------')

