# 通过for...in...能够一个个遍历出元素的对象，这个元素就是可迭代对象


# 可迭代对象的定义
# 实现一个__iter__方法
# __iter__方法返回的是一个迭代器对象


# 可迭代对象的本质
# 其实都是collections（容器数据类型） 模块里的Iterable类创建出的实例

# 查看是否为可迭代对象 isinstance(obj, Iterable)
from collections.abc import Iterable
print(isinstance([1,2.3,4], Iterable))