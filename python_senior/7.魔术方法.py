# 魔术方法
# class A:
#     pass
#
# print(dir(A))  # 输出所有属性和方法

# __doc__ 表示类的描述信息--注释内容

class A:
    """这是类的描述信息"""
    pass


print(A.__doc__)

# module 表示当前操作对象在那个模块
from b import Test

obj = Test()
print(obj.__module__)

# __class__ 表示当前操作的对象的类是什么（读取类名）
print(obj.__class__)


# __call__ 允许类能像实例一样去调用实例方法
class A:
    def __call__(self):
        print("__call__")


a1 = A()
a1()  # 表示自动调用call方法

# __dict__ 查看类或对象中的所有属性
class A:
    def __init__(self):
        self.a = 1
    def func(self):
        print('1111')

print(A.__dict__)

#__repr__ 改变对字符串的显示方式 __str__ 给用户看的 __repr__ 给程序员DEBUGGER的
class A:
    def __repr__(self):
        return 'hello'

a = A()
print(a)

# __getitem__ __setitem__ __delitem__ 实现类似字典的操作 设置、删除、获取
class A:
    def __getitem__(self, item):
        print('111111111111', item)
    def __setitem__(self, key, value):
        print('22222222222222', key, value)
    def __delitem__(self, key):
        print('33333333333333333333', key)

tex = A()
te = tex['name']
tex['name'] = 'zsss'
del tex['name']