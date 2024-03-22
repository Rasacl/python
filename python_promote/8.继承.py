# 继承
# 继承克可以使得子类自动拥有父类的属性和方法，这样可以减少不必要的重复代码。

# 继承的优点
# 1. 代码重用
# 2. 提高代码可读性
class God:
    def sing(self):
        print('sing')
    def dance(self):
        print('dance')


class Person(God): # Person类从God类继承
    pass


# 创建对象
p = Person()
p.sing()

# 新式类与旧式类
# python3中定义类 新式类
class A(object):
    pass
class B():
     pass
class C:
    pass


#在python2.x的版本中，默认都是经典类，如果需要使用新式类，需要显式的继承object类，才会是新式类