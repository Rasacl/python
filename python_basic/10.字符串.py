# encode编码 将字符串转换为字节流（二进制数据流）
a='hello'
al = a.encode()
print(al)

# decode解码 将字节流（二进制数据流）转换为字符串
b=b'\x68\x65\x6c\x6c\x6f'
bl = b.decode()
print(bl)

# 索引 获取指定位置的字符 索引从0开始 负数表示从末尾开始计算 索引越界时，抛出异常 IndexError
a = 'hello'
print(a[1])
print(a[-2])

# 字符串切片 返回一个新的子串，起始索引包含，结束索引不包含 索引从0开始 负数表示从末尾开始计算 索引越界时，截取有效范围内的字符串 [开始索引:结束索引:步长]
# 指定区间时，左闭右开
# 步长为正数时，从左向右取值 步长为负数时，从右向左取值 步长为0时，抛出异常 ValueError 步长必须为整数
e = 'hellofergerfgfererer'
print(e[1:5])
print(e[-4:-1])
print(e[::2])
print(e[:])  #没有限制，取到所有


# 字符串查找 1. find 查找子串首次出现的位置 未找到子串时，返回-1 find(str, 开始下标， 结束下标)
c = 'edwwewewewewewefdcfd'
print(c.find('e'))

# index 查找子串首次出现的位置 未找到子串时，抛出异常 ValueError index(str, 开始下标， 结束下标)
d = 'edwwewewewewewefdcfd'
print(d.index('we'))

# count 统计子串出现的次数 count(str, 开始下标， 结束下标)
f = 'vfvrtgtygrfwefwe'
print(f.count('f'))

# replace 替换字符串中的子串 replace(旧子串, 新子串, 替换次数)
g = 'vfvrtgtygrfwefwe'
print(g.replace('f', 't'))

# split  按照指定的分隔符拆分字符串 返回一个包含拆分后的子串的列表 split(分隔符, 最大分割次数)
h = 'dn,vi,rf,ld,uj,dlf'
print(h.split(','))

# capitalize 首字母大写
i = 'vfvrtgtygrfwefwe'
print(i.capitalize())

# lower 转换为小写
j = 'VfvRtgTyGrFwefwe'
print(j.lower())

# upper 转换为大写
k = 'VfvRtgTyGrFwefwe'
print(k.upper())

# title 每个单词首字母大写
l = 'hh lo bnh'
print(l.title())

# 判断 isalnum 是否为字母或数字 isalpha 是否为字母 isdigit 是否为数字 islower 是否为小写 isspace 是否为空白字符 istitle 是否为首字母大写 isupper 是否为大写

# startswith 以指定子串开头 endswith 以指定子串结尾
m = 'hellofergerfgfererer'
print(m.startswith('he'))
print(m.endswith('rer'))

# 增 将一个字符串附加到另一个字符串末尾 返回拼接后的新字符串
n = 'hello'
print(n + 'world')

# join 将序列中的元素以指定的字符串连接起来 返回连接后的新字符串
o = 'hello'
print('*'.join(o))

#删 lstrip 移除字符串左侧的空格和指定字符 rstrip 移除字符串右侧的空格和指定字符 strip 移除字符串两侧的空格和指定字符
p = '  hello world  '
print(p.lstrip())
print(p.rstrip())
print(p.strip())