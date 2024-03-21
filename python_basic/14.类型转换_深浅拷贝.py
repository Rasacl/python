# 类型转换 number string list dict tuple set

# int() float() str() bool() list() tuple() set() dict()
print(int('123'))  # 123
print(float('12.3'))  # 12.3
print(str(1.23))  # '1.23'
print(bool(1))  # True
print(list((1, 2, 3)))  # [1, 2, 3]
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set({1, 2, 3}))  # {1, 2, 3}
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# 深浅拷贝
# 浅拷贝 浅拷贝只复制了对象，没有复制它所引用的对象
import copy
a = [1, 2, [3, 4]]
b = copy.copy(a)
print(id(a))  # [1, 2, [100, 4]]
print(id(b))

# 深拷贝 深拷贝不仅复制了对象，还复制了它所引用的对象
import copy
c = [1, 2, [3, 4]]
d = copy.deepcopy(c)
d[2][0] = 100
print(c)
print(d)

# 小结
'''
深拷贝 深拷贝不仅复制了对象，还复制了它所引用的对象 
浅拷贝 浅拷贝只复制了对象，没有复制它所引用的对象 第一层数据可以完全复制  第二层开始，只复制了引用，没有复制数据
应用场景 深拷贝一般用于不可变的对象，浅拷贝一般用于可变的对象, 
'''