# multiprocessing模块 提供一个process类
# Process([group[,target[,name[,args[,kwargs]]]])
"""
target 表示调度对象，即子进程执行的任务
args 给target指定函数传递的参数 元组类型
kwargs 给target指定函数传递的参数 字典类型
name 进程的名字，方便跟踪
group 进程组，一般不使用
"""

# 常用属性
# name 当前进程的别名 默认Process-N N从1开始递增
# pid 当前进程的进程号
# ppid 当前进程的父进程号


# os 模块提供了很多操作系统相关的函数

# 创建进程简单实现
import os
from multiprocessing import Process
def one():
    print('one子进程id:%s,父进程id：%s' % (os.getpid(), os.getppid()))

def two():{
    print('two子进程id:%s,父进程id：%s' % (os.getpid(), os.getppid()))
}


if __name__ == '__main__':
    p1 = Process(target=one)
    p2 = Process(target=two)
    p1.start()
    p2.start()

    # 修改进程名
    p1.name = 'one_process'
