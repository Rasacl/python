from multiprocessing import Process,Queue
import time
import random

list = [1,2,3,5]

def write(q):
    for i in list:
        print(f'将{i}放入队列')
        q.put(i)
        time.sleep(random.random())


def read(q):
    while True:
      if not q.empty():
          info = q.get()
          print(f'从队列中获取{info}')
          time.sleep(random.random())
      else:
          break


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()

    print('这是主程序')