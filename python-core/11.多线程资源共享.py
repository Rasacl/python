from threading import Thread
import  time
list = []

def writedata():
    for i in range(10):
        list.append(i)
        time.sleep(0.001)
    print('写入数据',list)

def readdata():
    print('读取数据',list)


if __name__ == '__main__':
    t1 = Thread(target=writedata)
    t2 = Thread(target=readdata)
    t1.start()
    t1.join()
    t2.start()
    print('主线程')