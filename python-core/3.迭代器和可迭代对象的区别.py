# 迭代器 Iterator 可迭代对象 Iterable

# 区别
# 凡是可以调用__iter__()方法的对，即它是一个可迭代对象。
# 凡是可以调用next()方法的，即它是一个迭代器。
from collections.abc import Iterable,Iterator
list = [1,2,3,4]
s = iter(list)
print(isinstance(list,Iterable)) # True
print(isinstance(s,Iterator)) # True