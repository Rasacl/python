# 1. 反转字典
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
redict = dict(map(reversed, my_dict.items()))
print(redict)

# 对字典列表进行排序
dict_list = [
    {'name': '张三', 'age': 30},
    {'name': '李四', 'age': 25},
    {'name': '王五', 'age': 28}
    ]
dict_list.sort(key=lambda x: x['age'])
print(dict_list)

# 3 根基另一个列表对一个列表进行排序
a = ['blue', 'red', 'green', 'orange', 'yellow']
b = [3,2,5,4,1]
sortList =[val for (_, val) in sorted(zip(b,a),key=lambda x:x[0])]
print(sortList)

# 4 把两个列表合并到一个字典
key_list = ['A', 'B', 'C']
val_list = ['blue', 'red', 'yellow']

dict_re = dict(zip(key_list,val_list))
print(dict_re)

# 5 对字符串列表进行排序
my_list = ['blue', 'red','green']
my_list.sort()  # 字母顺序排序
print(my_list)
print(sorted(my_list, key=len)) # 根据字符串长度排序


# 检查文件是否存在
import os

print(os.path.isfile(r'F:\python\爬虫\2.http2.0爬虫解决方案.py')) # 文件夹用exists

