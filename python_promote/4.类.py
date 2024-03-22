# 类
# class 类名:  类名习惯使用大驼峰命名 首字母大写 私有类可用一个下划线开头
#     pass    里面什么内容都没有 表示这个类是一个空类 没有属性和方法 可用pass
#
# class 类名:
#     成员

class Hello(object): # object是python里所有类的最顶级的父级
    def info(self):  # info 是实例方法 第一个参数一般是self 表示实例本身 也可以取别的名字，其作用是这个变量指向这个实例对象
        print("Hello World!")


# 属性: 对象的特征描述（实际上为类中定义的变量，该变量为属性）
# 方法： 对象具有的行为（本质是函数），类中定义的函数即为方法

# 对象的创建 对象名 = 类名()
h = Hello()

h.info()

class Student:
    name = "张三"
    def info(self):
        print(1234)


print(Student.__dict__) # 查看类的属性
print(Student.__dict__['name'])

# 增删改查类中的单个属性
print(Student.name)
Student.name = "李四"
print(Student.name)
del Student.name
Student.walk = '走路'
print(Student.walk)


# 添加对象的属性和方法
# 添加和获取对象的属性
s = Student()
s.age = 10
print(s.age)
print(s.__dict__)

# 在方法内通过self获取对象属性
class A:
    def test(self):
        print('%s的年龄是%d'%(self.name, self.age))

a = A()
a.name = '张三'
a.age = 10
a.test()

# 类属性属于类 实例属性属于对象

class B:
    num = 0
    def __init__(self, name):
        self.name = name
    def test(self):
        print(f'我的名字是{self.name}')

b = B('李四')
print(b.name)