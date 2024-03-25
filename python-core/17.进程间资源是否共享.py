# 进程不同享全局变量
from multiprocessing import Process
import time

list = []

def funa():
    for i in range(3):
        list.append(i)
        time.sleep(1)
        print('这是funa子进程中的',list)

def funb():
    print('这是funb子进程中的',list)


if __name__ == '__main__':
    p1 = Process(target=funa)
    p2 = Process(target=funb)
    p1.start()
    p2.start()


