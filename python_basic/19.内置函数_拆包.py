# 内置函数
import builtins # 导入内置函数模块
print(dir(builtins))

# reduce 函数
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# enumerate 函数 枚举 用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列， 同时列出数据的列表 一般用于 for 循环中
for i, value in enumerate(['apple', 'banana', 'cherry']):
    print(i, value)



# 拆包 对于函数中多个返回的数据 去掉元组 列表或者字典，直接获取里面数据的过程
# 元组拆包
def get_data():
    a =10
    b=20
    c= 30
    return a, b, c

a,b,c = get_data()
print(a,b,c)

tu = (1,3,45,4)

a, *c,b = tu
print(a,c,b)

# 列表拆包
li = [1,2,3,4,5]
a, b, *c, d = li
print(a,b,c,d)

# 字典拆包
di = {'a':1,'b':2,'c':3,'d':4}
a, b, *c, d = di
print(a,b,c,d)
