# 类中封装数据
import pr


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def add(self):
        print('姓名是：%s, 年龄是%d'%(self.name, self.age))

s = Student('张三', 20, 89)
s.add()

# 1.类的私有属性和私有方法，都不能通过对象直接访问，但是可以在本类内部访问
# 2.类的私有属性和私有方法，不能被子类继承，子类也无法访问
#3. 类的私有属性和私有方法往往是用来处理类内部的事情

# 定义私有属性和方法
# _x 也代表私有方法和属性，实际上类对象和子类可以访问
# __x 真正的私有成员，类对象和子类无法访问

# class Classmate:
#     name = 'lucy'
#     _age = 18
#     __sex = '女'

# c = Classmate()
# print(Classmate.name)
# print(Classmate._age)
# # print(Classmate.__sex)
# # 强行获取私有属性
# print(c._Classmate__sex)
# print(c.name)
# print(c._age)
# print(c.__sex)

# 正规手段访问私有属性
'''
1. 在类的内部的公有方法中访问私有属性和私有方法
2.在外部调用公有方法，以间接的使用私有属性
'''
class Classmate:
    def __init__(self):
        self.__name = 'lucy'

    def funa(self):
        print(self.__name)

    def __test(self):
        print(121324)

    def test1(self):
        self.__test()

p = Classmate()
p.funa()
p.test1()

# 修改私有属性 通过公共方法去修改