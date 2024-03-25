# 遍历很大的数据集合 节省内存 不依赖索引值 实现惰性计算

class Person:
    # def __init__(self):
    #     self.n = 1
    # def funa(self):
    #     self.n += 1
    #     return self.n

    #修改成迭代器
    def __iter__(self):
        self.n = 1
        return self
    def __next__(self):
        self.n += 1
        return self.n
a = Person()
my = iter(a)
print(next(my))
from collections.abc import Iterator,Iterable
print(isinstance(a,Iterator))
print(isinstance(a,Iterable))