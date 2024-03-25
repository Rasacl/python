# 定义一个线程类
# 1.继承Thread方法
# 2.重构run方法

from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        print('重温对象')
        time.sleep(2)
        print('你们还找的到吗')


if __name__ == '__main__':
    # 创建线程
    t1 = MyThread()
    t1.start()


# start 和run的区别
'''
start方法：是声明分到一个子进程的函数已经就绪 等待被cpu执行
run方法：是线程要执行的具体内容
'''