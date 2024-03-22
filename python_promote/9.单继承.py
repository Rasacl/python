# 单继承
class A:
    Sname='动物类'
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def eat(self):
        print(f'{self.name}在吃东西, 性别是{self.sex}，年龄是{self.age}')


class Dog(A):
    pass

p1 = Dog('旺财','male',3)
p1.eat()

# 继承的传递性
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name}在吃东西')
    def sleep(self):
        print(f'{self.name}在睡觉')


class Dog(Animal):
    def bark(self):
        print(f'{self.name}在汪汪叫')


class BlackDog(Dog):
    def fly(self):
        print(f'{self.name}会飞')


black = BlackDog('小黑')
black.eat()
black.sleep()
black.bark()
black.fly()