# 单例模式 是一个特殊的类，这个类只能够创建一次实例对象
# 单例模式 让所有的类在实例化时，指向同一个内存地址
# 为什么要有单例模式
# 节省内存空间，因为产生不同的对象，会产生不同的内存地址，造成资源浪费
# 设置单例模式的本质 判断这个实例是否存在，如果存在，直接返回，不存在，创建实例，并赋值给成员变量

# __new__创建单例模式
class Test(object):
    ins = None

    def __new__(cls, *args, **kwargs):
        if cls.ins is None:
            cls.ins = super().__new__(cls)
        return cls.ins


# p = Test()
# p1 = Test()
# print(id(p))
# print(id(p1))


# 类创建单例模式
class Test2(object):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)

        return Test2.instance


# a = Test2.get_instance()
# b = Test2.get_instance()
# print(id(a))
# print(id(b))

# 装饰器创建单例模式
def outer(fn):
    _ins = {}

    def inner():
        if fn not in _ins:
            _ins[fn] = fn()
        return _ins[fn]

    return inner


@outer
class A(object):
    a = 1

# a = A()
# b = A()
# print(id(a))
# print(id(b))


# 通过导入模块实现单例模式
from test import B
from test import B
# python的模块时天然的单例模式，因为模块第一次导入会加载到内存空间中，再次导入时，直接从内存中获取

# 通过元类实现单例模式 hasattr() 方法判断类中是否存在指定的属性
# 参数是一个对象和一个字符串，如果字符串是对象的属性值，返回True，否则返回False
# class A:
#     b= 3
#     def test(self):
#         print('test')
#
# print(hasattr(A(), 'b'))
# print(hasattr(A(), 'test'))

class N:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'ins'):
            cls.ins = super().__new__(cls)
        return cls.ins


s = N('里斯')
V = N('看看')
print(id(s))
print(id(V))