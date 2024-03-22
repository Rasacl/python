# @staticmethod
# def 方法名():
#     方法体

# 静态方法是类中的函数，它不需要实例，可以理解为是独立，单纯的函数
class Dog(object):
    age = 10
    @staticmethod
    def bark():
        print("The dog broke the door.")

    @staticmethod
    def get_age():
        return Dog.age

dog = Dog()
dog.bark()
print(dog.get_age()) # 实例对象可以去访问静态方法
print(Dog.get_age()) # 类对象可以访问静态方法