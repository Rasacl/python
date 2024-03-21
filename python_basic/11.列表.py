# 列表 一次性存储多个数据
li = [1,2,3,4,5]
print(li[0])

for i in li:
    print(i)


len = len(li)
i = 0
while i < len:
    print(li[i])
    i+=1


# 增加元素 +
a = [1,3,4]
b = [5.67,89,0]
c= a+b
print(c)

# insert 插入元素 insert(index, obj) 在index前插入obj
d = [1,2,3]
d.insert(1,4)
print(d)

# append 增加元素 append(obj) 将obj添加到列表末尾
e = [1,2,3]
e.append(4)

# extend 增加列表 extend(list) 将list中的元素逐个添加到列表末尾
f = [1,2,3]
g = [4,5,6]
f.extend(g)
print(f)


# 修改元素 修改列表中位置index的元素为obj
h = [1,2,3,4,5]
h[1] = 6
#修改一组元素
h[1:3] = [7,8]

# 特殊情况 对空切片赋值 对应下标前插入所有的元素
h[1:1] = [9,10]

# 删除 删除单个元素 del 列表名[索引]
i = [1,2,3,4,5]
del i[2]
print(i)
del i[2:5] # 删除范围 删除多个值
del i

#pop 删除并返回最后一个元素 pop(index)  index不写，默认删除最后一个元素
j = [1,2,3,4,5]
j.pop(2)
print(j.pop())


# remove 删除指定元素 remove(obj) 删除第一个等于obj的元素
k = [1,2,3,4,5]
k.remove(3)

# clear 清空列表 clear()
l = [1,2,3,4,5]
l.clear()


# 查找元素

# in 检查元素是否在列表中
m = [1,2,3,4,5]
print(2 in m)

# not in 检查元素是否不在列表中
n = [1,2,3,4,5]
print(6 not in n)

# count() 统计某个元素在列表中出现的次数
o = [1,2,3,4,5,2,3,4,5,6,7,8,9,10]
print(o.count(2))

# index() 找到某个元素在列表中的第一个位置 index(obj, startindex , endindex)
p = [1,2,3,4,5,2,3,4,5,6,7,8,9,10]
print(p.index(2))

# 排序
# sort() 对原列表进行排序 sort(reverse=False) reverse=True 降序排列
q = [1,5,4,88,3,8,243]
q.sort()

# reverse() 对原列表进行反转 reverse()
r = [1,5,4,88,3,8,243]
r.reverse()
print(r)


# 扩展
# sort只适用于list排序
# 使用sorted函数可以对任意可迭代对象进行排序
s = [1,5,4,88,3,8,243]
t = sorted(s) # 默认从小到大排序，不能对源列表进行修改
print(t)


# 列表表达式
print([i * 3 for i in [1,4,6,7,3]])