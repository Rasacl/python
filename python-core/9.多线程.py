# 多线程
# 线程类参数： group：线程组  target：目标函数  name：线程名称  args：目标函数参数  kwargs：关键字参数
# 1 导入模块
import threading
# 2 创建子线程 Thread（）类

# 3 守护线程 守护线程就是程序结束时，该线程会自动结束  setDaemon(True)

# 4 启动线程 start()

# 5 阻塞主线程 让主线程等待子线程结束 join()


import time
import threading

def funa():
    print("funa is running")
    time.sleep(2)
    print("funa is finished")

def funb():
    print("funb is running")
    time.sleep(3)
    print("funb is finished")

if __name__ == "__main__":
    t1 = threading.Thread(target=funa)
    t2 = threading.Thread(target=funb)
    #设置守护线程
    # 设置守护线程
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()

    # 阻塞主线程
    t1.join() # 等待t1线程结束
    t2.join() # 等待t2线程结束

    print('这是主进程')



# 多线程的意义和应用场景
'''
多线程并不是多个线程并发在同一时间点运行，而是cpu有计划的交替执行多个线程
'''