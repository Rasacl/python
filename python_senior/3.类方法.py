# 类方法 在类方法的内部可以直接访问类属性或调用类方法
# class 类名():
#     @classmethod -- 类方法标识
#     def 方法名(cls): -- 第一个参数必须时cls（代表当前类名）
#         方法体

# 类方法内部使用类属性 cls.属性
# 类方法内部使用类方法 cls.方法（）
# 类方法的本质 将类本身作为对象进行操作的方法

class Person:
    age =20
    @classmethod
    def human_age(cls):
        return cls.age

    @classmethod
    def get_age(cls):
        return  cls.age

    @classmethod
    def set_age(cls,age):
       cls.age = age

p = Person()
print(p.human_age()) # 实例对象可以访问类方法
print(Person.human_age())

# 修改类属性
print(Person.get_age())
Person.set_age(25)
print(Person.get_age())
