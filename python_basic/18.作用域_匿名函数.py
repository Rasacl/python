# 作用域  全局作用域 和 局部作用域

# global 将变量声明为全局变量，这样在函数内部就可以修改全局变量的值

a = 100
def test():
    global a
    a = 10
    print(a)

def test2():
    print(a)

test()
test2()

# nonlocal 将变量声明为非全局变量，这样在函数内部就可以修改外部函数的变量的值 不能修改全局变量的值 对父级作用的变量进行修改，并且引用的那层，就从那层开始往下，此变量全部发生改变
a = 10
def funa():
    a = 1
    def funb():
        nonlocal  a
        print('funb函数中b的值', a)
        a = 2
    funb()
    print('funa函数中a的值', a)

funa()
print('全局a的值', a)

# 匿名函数 lambda 函数 使用场景：当函数只有一个表达式时，可以使用lambda函数，简化代码
def square(x):
    return x * x
print(square(5))
print((lambda x: x * x)(5))

func = lambda a,b: a * b
print(func(3,4))

# 在字符串中，返回索引为0和2的元素
str='efwewefwee'
funv = lambda x:[x[0],x[2]]
print(funv(str))