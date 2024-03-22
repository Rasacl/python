# 多继承 子类可以拥有多个父类，并且具有所有父类的属性和方法Z
# class A:
#     def speak(self):
#         print("Animal speak")
#
# class B:
#     def dome(self):
#         print("Bird dome")
#
# class C(A,B):
#     pass
#
# c= C()
# c.speak()
# c.dome()

# 如果不同父类中有相同名的方法，那么在子类中调用该方法时，将调用最上层父类中的方法。
# class A:
#     def speak(self):
#         print("Animal speak")
#
#     def play(self):
#         print("A play")
#
# class B:
#     def dome(self):
#         print("Bird dome")
#     def play(self):
#         print("B play")
#
#
# class C(A,B):  # 就近原则 谁先继承就先用谁
#     pass
#
# c = C()
# c.play()
# # 查看c类调用方法的顺序
# print(C.__mro__)

print('==========================================================================')
# 如果多个父类中有同名的属性和方法时 默认使用继承的第一个父类的属性和方法

class A:

    def play(self):
        print("A play")

class B:
    def play(self):
        print("B play")


class C(A,B):
    def play(self):
        A.play(self)
        super().play()

c = C()
c.play()