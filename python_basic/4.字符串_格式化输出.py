str = 'hello'
print(type(str))

str2 = '''
 hei
 hfhfe
 fefe
'''
print(str2)

print("hello \"w\"dfd")

# 字符串的运算
print('heool' + 'fdfdf')

# * 表示重复次数 复制字符串
print('heool' * 5)

# in 操作符 判断字符是否在字符串中
a = 'hello'
print('h' in a)
# not in 判断字符是否不在字符串中
print('h' not in a)

# r\R 原样输出内容
print(r'\n')

# 格式化输出 定义一个模板 按照模板输出内容

# %s 字符串
age = 18
name = 'tmo'
print('%s is %d years old' % (name, age))

# %f 浮点数
ad = 1.24354566
print('%f' % ad) # 默认保留六位小数
print('%.2f' % ad) # 保留两位小数

# 十进制
print('%d' % 12.345)

# 八进制
print('%o' % 9)

# format 方法 使用{}占位符 和 .format() 方法 括号
print('{0} is {1} years old'.format(name, age))
print('{name} is {age} years old'.format(name=name, age=age))
