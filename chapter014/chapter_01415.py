# 线程池执行程序1：
from concurrent.futures import ThreadPoolExecutor
import time


# 执行函数
def func(n):
    time.sleep(1)
    print(n)
    return n * n


# 线程池对象
print("----------------启动主线程-------------------")
thread_pool = ThreadPoolExecutor(max_workers=5)
thread_list = []
#
for i in range(10):
    # 执行任务，传递参数
    r = thread_pool.submit(func, 2)
    # 获取任务返回结果
    thread_list.append(r.result())

thread_pool.shutdown()  # 相当于close() + join()
print(thread_list)
print('---------------主线程运行结束------------------')