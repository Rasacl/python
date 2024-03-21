def merge_sort(arr):
    return arr


num = merge_sort([1.3,5,7,3])

print(num)

# 必选参数 定义几个就必须传递几个
def function_name(a, b):
    return  a- b


function_name(1,5)


# 默认参数
def function_name(a, b=3):
    return a - b


# 可变参数 *args 接收多个值时，以元组的形式接收
def function_name(*args):
    return args

b = function_name(1,4,56,6)
print(b)


# 关键字参数 **kwargs 接收多个值时，以字典的形式接收
def function_name(**kwargs):
    print(kwargs)

function_name(name='xixi',age=12)


# 匿名关键字参数 使用参数名
def function_name(name,age,*,city='shanghai',job='coder'):
    print(name,age,city,job)

function_name('cc',12,job='eator')


# 扩展 混合参数
# 参数定义顺序 必选参数 默认参数 可变参数 命名关键字参数 关键字参数
def name(a,b=1,*args,c=3,**kwargs):
    print(a,b,args,c,kwargs)

# 调用·1
name(1,2,3,4,5,c=6,d=7)


# 函数嵌套 在函数内部调用另一个函数
def funa():
    print('a')

def funb():
    print('innr')
    funa()


funb()


