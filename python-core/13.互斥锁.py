
# 互斥锁 线程同步 目的是按顺序执行

# 互斥锁 能够保证多个线程访问共享数据不会出现数据错误的问题 对共享数据进行锁定，保证同一时刻只能有一个线程操作

# 互斥锁的使用：
"""
threding.Lock() 创建一个锁对象
acquire() 获取锁，如果锁未被占用，立即返回，否则阻塞，直到锁可用才返回
release() 释放锁，将锁的状态设为未占用，如果有其他线程在等待锁，将锁分配给等待时间最长的线程
"""

from threading import Thread,Lock
a = 0
b = 100
lock = Lock()
def sum():
    lock.acquire()
    for i in range(b):
        global a # a为整数 修改值时引用地址会发生改变 需声明
        a += 1
    print(f'第一次；{a}')
    lock.release()

def sun():
    lock.acquire()
    for i in range(b):
        global a # a为整数 修改值时引用地址会发生改变 需声明
        a += 1
    print(f'第二次；{a}')
    lock.release()

if __name__ == '__main__':
    t1 = Thread(target=sum)
    t2 = Thread(target=sun)
    t1.start()
    t2.start()