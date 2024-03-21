 # 元组 不能被修改 因为元组不可被修改和删除 所以提高了代码编写的安全性
um_list = (1,2,3)

# 定义多个数据的元组
multi_data = ('apple', 'banana', 'cherry')

# 定义单个数据的元组，必须加一个逗号
single_data = ('apple',)

# index 方法返回元组中第一个匹配项的位置
print(multi_data.index('banana'))

# count() 方法返回参数在元组中出现的次数
print(multi_data.count('apple'))

# len() 方法返回元组的长度
print(len(multi_data))


# 扩展: 元组'可变'的情况
tuple1 = (1, 2, 3, ['apple', 'banana', 'cherry'])
tuple1[3].append('orange')
print(tuple1)

# 字典 字典是无序的 键值对 键必须是不可变的对象 值可以是任意对象 键必须是唯一的
dict1 = {'apple': 3, 'banana': 2, 'cherry': 5}
print(dict1['apple'])

# 增 改
dict1['orange'] = 4
print(dict1)
dict1['apple'] = 6
print(dict1)

# 删除
del dict1['banana']
print(dict1)
# dict1.clear()

# len() 方法返回字典元素的数量
print(len(dict1))

# values() 方法返回字典中的所有值
print(dict1.values())

# keys() 方法返回字典中的所有键
print(dict1.keys())

# items() 方法返回字典中的所有键值对列表
print(dict1.items())

# 字典的循环遍历
for key, value in dict1.items():
    print(key, value)