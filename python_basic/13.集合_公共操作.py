#  集合 大括号包围元素，每个元素有逗号隔开
# 与字典的区别 集合中没有键值对，字典中元素是键值对
my_set = {1, 2, 3, 4, 5}
print(my_set)

# set() 函数 将列表或其他可迭代对象转换为集合
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]
my_set = set(my_list)
print(my_set)

# 定义一个空集合
my_set = set()

# 集合的特性 无序不重复 不支持下标操作

# 集合的常用方法

# add() 方法 向集合中添加元素
my_set.add(1)

# update() 方法 向集合中添加可迭代的对象（列表、集合、元组、字典）
my_set.update([2, 3])
print(my_set)

# 删
# remove() 方法 从集合中删除指定的元素 如果数据不存在 会抛出KeyError异常
my_set.remove(1)

# pop() 方法 随机从集合中获取并删除一个元素 如果集合为空 会抛出KeyError异常
my_set.pop()

# discard() 方法 从集合中删除指定的元素 如果数据不存在 不会抛出异常
my_set.discard(2)

# & 交集 两个集合具有相同的元素 返回一个新集合
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)

# | 并集 返回一个新集合 包含所有元素
print(set1 | set2)

# ___________________________________________________________________________________________________________________________________

#公共操作

# + 字符串连接 列表拼接 元组

# * 复制 列表 字符串 元组

# in n ot in 列表 字符串 元组 字典

# 公共方法

# len() 列表 字符串 元组 字典 集合都适用

# del 删除 列表 字典 字符串

#max() 列表 字符串 元组 字典 集合 最大值
list = [1,3,5,7]
print(max(list))
#min() 列表 字符串 元组 字典 集合 最小值
print(min(list))

# range() 生成一个整数列表 起始值 结束值 步长

# enumerate() 用于枚举一个可遍历的数据类型 返回索引值和元素
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)



# 列表推导式
list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in list]
print(new_list)

# 元组推导式
t= (1, 2, 3, 4, 5)
t1 = (x * 2 for x in t)
print(tuple(t1),1111)

# 字典推导式
d = {'a': 1, 'b': 2, 'c': 3}
d1 = {k: v * 2 for k, v in d.items()}
print(d1)

# 集合推导式
s = {1, 2, 3, 4, 5}
s1 = {x * 2 for x in s}
print(s1)