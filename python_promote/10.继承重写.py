# 继承重写
class human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating' % self.name)


class student(human):
    def eat(self):
        print('%s is studying' % self.name)


s = student('里斯', 66)
s.eat()


# 扩展父类方法

class Animal(object):
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def eat(self):
        # Animal.eat(self) 或者 super().eat()
        super().eat()
        print('啃骨头')


b = Dog()
b.eat()


# 继承父类方法并进行改写
class S(object):
    def __init__(self, name):
        self.name = name
        print('父类中的名字是', self.name)

    def test(self):
        print('父类中的%s在哈哈笑' % self.name)


class A2(S):
    def __init__(self, name):
        super().__init__(name)  # 修正：使用super()调用父类的__init__方法 (保留父类相关内容)
        self.name = name
        print('子类中的名字是', self.name)

    def test(self):  # 对父类进行重写（覆盖写）
        print('12312312434')


a = A2('阙清')
a.test()
