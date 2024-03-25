from multiprocessing import Pool,Manager
import os
def rd(q):
    print(f'rd启动{os.getpid()},父进程{os.getppid()}')
    for i in range(q.qsize() ):
        print(f'读取数据{q.get()}')


def wd(q):
    print(f'wd启动{os.getpid()},父进程{os.getppid()}')
    for i in '123':
        print('wd中的 ', i)
        q.put(i)

 
if __name__ == '__main__':
    print('开始了',os.getpid())
    q = Manager().Queue()
    p = Pool()
    p.apply_async(wd, (q,))
    p.apply_async(rd, (q,))
    p.close()
    p.join()
    print('结束')