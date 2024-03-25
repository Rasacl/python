from threading import Thread
a = 0
b = 1000000

def sum():
    for i in range(b):
        global a # a为整数 修改值时引用地址会发生改变 需声明
        a += i
    print(f'第一次；{a}')

def sun():
    for i in range(b):
        global a # a为整数 修改值时引用地址会发生改变 需声明
        a += i
    print(f'第二次；{a}')

if __name__ == '__main__':
    t1 = Thread(target=sum)
    t2 = Thread(target=sun)
    t1.start()
    t2.start()


# 解决办法 1.  使用threading.Lock() 保证线程安全 2. 使用进程等待 join() 方法
