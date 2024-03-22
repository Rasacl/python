# __init__ 初始化设置--实例对象创建是会自动调用的方法
# __new__ 是第一个创建对象时真正被调用的方法

# __new__的作用 -- 如果不设置，系统会默认设置
# 1.在内存中为对象分配空间
# 2.返回对象的引用 返回值会引发__init__调用

#__new__ 没有返回值的情况
# class A:
#     def __new__(cls, *args, **kwargs):  # 创建实例时，第一个调用__new__
#         print("new", cls)
#     def __init__(self):
#         print("init")
#
# p = A()
# print('这是类', A)

# 重写
class A(object):
    def __new__(cls, *args, **kwargs):  # 创建实例时，第一个调用__new__
        print("new", cls)
        # return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self):
        print("init")

p = A()
print('这是类', A)


# __new__与__init__的区别
'''
__new__时真正在创建实例对象时被第一个调用的方法，该方法返回对象的引用时，用__init__的调用
__new__的第一个参数是cls，__init__的第一个参数是self
__new__必须有返回，且返回的是对象的引用，否则__init__不会调用
'''