# 线程池：任务执行结束判定2
from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


# 线程池执行器
executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]    # 并不是真的url
# 无需提交任务，等待任务结束
for data in executor.map(get_html, urls):
    print("in main: get page {}s success".format(data))