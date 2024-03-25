import os
import time
from multiprocessing import Pool

# # 异步
# def learn(n):
#     print('我们在做学术交流')
#     time.sleep(3)
#     return n**2
#
#
# if __name__ == '__main__':
#     p = Pool(3)
#     list = []
#     for i in range(6):
#         # apply_async 异步调用，不会阻塞，可以同时进行多个任务
#         result = p.apply_async(learn, (i,))
#         list.append(result)
#     p.close()
#     p.join()
#
#     for j in list:
#         print(j.get())



# 同步 apply 调用，会阻塞，只能一个一个任务执行

def learn(n):
    print('我们在做学术交流')
    time.sleep(3)
    return n**2

if __name__ == '__main__':
    p = Pool(3)
    list = []
    for i in range(6):
        result = p.apply(learn, (i,))
        list.append(result)

    p.close()
    p.join()

    for j in list:
        print(j)
