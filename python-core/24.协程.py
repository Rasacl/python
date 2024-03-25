# 协程 单线程下的并发 又称为微线程 纤程
# 是一种用户态的轻量级线程 由操作系统直接支持 切换成本小
# 协程能保留上一次调用的状态 线程和进程通过cpu调度 对于协程来说 程序员就是上帝 你想让他执行就执行

# 协程存在的意义
'''
多线程：分时切片 并发操作 线程切换需要耗时
协程 只使用一个线程 在一个线程中规定某个代码执行顺序
'''

# 使用yield实现协程
import time
def producer():
    while True:
        yield '好好学习'
        time.sleep(0.5)


def work():
    while True:
        yield '突然喜爱你'
        time.sleep(0.5)

if __name__ == '__main__':
    p = producer()
    w = work()
    while True:
        print(next(p))
        print(next(w))
